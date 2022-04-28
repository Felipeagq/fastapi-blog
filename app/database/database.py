from typing import Any
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from app.settings import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    # connect_args={
    #     "check_same_thread":False
    # }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()


@as_declarative()
class Base:
    id: Any
    __name__:str
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__tablename__.lower()