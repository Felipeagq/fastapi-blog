from datetime import date, datetime
from pydantic import BaseModel
from typing import List,Optional

class BlogRequestSchema(BaseModel):
    title:str
    body:str
    date:str 


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    

class BlogShowUserSchema(BaseModel):
    title: str 
    class Config:
        orm_mode = True


class UserShowIdResponse(BaseModel):
    username: str
    email: str
    blogs: List[BlogShowUserSchema]
    class Config:
        orm_mode = True


class UserBlogResponseSchema(BaseModel):
    username:str
    email:str
    class Config:
        orm_mode = True


class BlogResponseSchema(BaseModel):
    title:str
    body:str
    creator: UserBlogResponseSchema
    class Config:
        orm_mode = True
        
        
class LoginSchema(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str = None
    # username: Optional[str] = None
    # email: Optional[str] = None
