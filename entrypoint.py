from sys import prefix
from fastapi import FastAPI
from app.settings import settings

from starlette.middleware.cors import CORSMiddleware

from app.routes import blog_management
from app.routes import user_management
from app.routes import login_management

app = FastAPI(
    title= settings.PROJECT_NAME,
    version= settings.PROJECT_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def hello_check():
    return {
        "PROJECT_NAME":settings.PROJECT_NAME,
        "PROJECT_VERSION": settings.PROJECT_VERSION
    }


app.include_router(blog_management.router, prefix=settings.API_V1_STR)

app.include_router(user_management.router,prefix=settings.API_V1_STR)

app.include_router(login_management.router, prefix=settings.API_V1_STR)