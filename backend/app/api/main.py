from fastapi import APIRouter
from app.api.routes import avatar, users

api_router = APIRouter()

api_router.include_router(avatar.router, prefix="/avatar", tags=["avatar"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
