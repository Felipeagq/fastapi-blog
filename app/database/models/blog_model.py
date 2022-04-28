from sqlalchemy import Column,String, Integer,ForeignKey
from app.database.database import Base

from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index = True)
    title = Column(String)
    body = Column(String)
    date = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("UserModel", back_populates="blogs")


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index = True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")