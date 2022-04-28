from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import blog_schema
from fastapi.security import OAuth2PasswordRequestForm
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database.models.blog_model import UserModel

from app.settings import Security
from datetime import timedelta

router = APIRouter(tags=["Login management"])


@router.post("/login")
def login(
    # request: blog_schema.LoginSchema,
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
)-> str:
    
    user = db.query(UserModel).filter(UserModel.username==request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User dont found"
        )

    user = user.first()
    if not Security.is_valid(request.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    # Create a jwt and returned
    print(user.username)
    subject = {
        "username":user.username,
        "id": user.id
    }
    id_to_jwt = user.id
    print(subject)
    access_token = Security.created_access_token(subject=id_to_jwt,expire_delta=timedelta(minutes=30))
    # return user
    
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }