from datetime import datetime
from fastapi import APIRouter, Depends, Response, status, HTTPException, Body

from app.database.base import Base,Blog
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.database.models.blog_model import UserModel
from app.schemas import blog_schema

from app.schemas.blog_schema import BlogRequestSchema, BlogResponseSchema
from app.schemas import blog_schema

from typing import Dict, List,Any,Union

from app.settings import get_current_user

router = APIRouter()






@router.get(
    "/blogs",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=List[BlogResponseSchema],
    tags=["Blog Management"]
    )
def get_blogs(
    db:Session = Depends(get_db),
    get_current_user:blog_schema.UserRequestSchema = Depends(get_current_user)
):
    blogs = db.query(Blog).all()
    print(get_current_user)
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blogs dont founded"
        )
    return blogs






@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema,
    tags=["Blog Management"]
    )
def get_blog_id(
    id:int,
    response:Response,
    db:Session = Depends(get_db)
):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="id not found"
        )
    return blog


@router.post("/post",tags=["Blog Management"])
def post_blog(
    blog_request:BlogRequestSchema = Body(...,
    title="Post Blog Body",
    description="Request body for post a blog"),
    db:Session = Depends(get_db)
):
    new_blog = Blog(
        title = blog_request.title,
        body = blog_request.body,
        date = datetime.now(),
        user_id = 12
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        "msg":"ok",
        "posted": new_blog
    }

@router.delete("/delete/{id}",status_code=status.HTTP_202_ACCEPTED,
    tags=["Blog Management"]
    )
def delete_blog_id(
    id:int,
    response:Response,
    db:Session = Depends(get_db),
):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="blog dont founded"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        "msg":"ok",
        "deleted post": blog
    }


@router.put(
    "/update/{id}",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Blog Management"]
)
def update_blog(
    id:int,
    response: Response,
    request_body_blog: BlogRequestSchema,
    db:Session = Depends(get_db)
):
    updated_blog = db.query(Blog).filter(Blog.id == id)
    if not updated_blog:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="blog dont founded"
        )
    updated_blog.update(dict(request_body_blog))
    db.commit()
    return {
        "msg":"ok",
        "state":updated_blog,
        "updated_blog":request_body_blog
    }



