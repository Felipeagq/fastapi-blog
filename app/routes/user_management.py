from fastapi import APIRouter,status, Depends, HTTPException

from app.database.base import UserModel
from app.database.database import get_db
from sqlalchemy.orm import Session

from app.schemas import blog_schema

from app.settings import Security



router = APIRouter(tags=["User managment"])


@router.post("/user", status_code=status.HTTP_202_ACCEPTED)
def create_user(
    request:blog_schema.UserRequestSchema,
    db:Session = Depends(get_db)
) -> str:
    new_user = UserModel(
        username = request.username,
        email = request.email,
        password = Security.get_password(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "msg":"ok",
        "new_user":new_user
    }


@router.get("/user/{id}", 
            response_model=blog_schema.UserShowIdResponse,
            status_code=status.HTTP_200_OK)
def user_by_id(
    id:int,
    db:Session = Depends(get_db)
) -> str :
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="user by id not found"
        )
    return user