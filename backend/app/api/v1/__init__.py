from fastapi import APIRouter

from core.config import settings
from .users import users_router
from .webhook import webhook_router

api_v1_router = APIRouter(prefix=settings.api.v1.prefix)
api_v1_router.include_router(users_router)
api_v1_router.include_router(webhook_router)
