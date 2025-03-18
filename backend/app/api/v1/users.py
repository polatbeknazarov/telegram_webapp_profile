from typing import List

from fastapi import APIRouter

from core.config import settings
from core.schemas.users import UserRead, UserCreate, UserUpdate
from core.models import User
from services import users

users_router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["Users"],
)


@users_router.post("", response_model=UserRead)
async def create_user(user_create: UserCreate):
    return await users.create_user(user_create=user_create)


@users_router.get("/{telegram_id}", response_model=UserRead)
async def get_user_by_telegram_id(telegram_id: int):
    return await users.get_user_by_telegram_id(telegram_id=telegram_id)


@users_router.patch("/set_birth_date", response_model=UserRead)
async def set_birth_date(user_update: UserUpdate):
    return await users.update_user_birth_date_field(user_update=user_update)


@users_router.get("", response_model=List[UserRead])
async def get_all_users():
    return await User.all()
