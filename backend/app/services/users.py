import logging

from tortoise.exceptions import IntegrityError
from fastapi import HTTPException, status

from core.models import User
from core.schemas.users import UserCreate, UserUpdate

log = logging.getLogger(__name__)


async def create_user(user_create: UserCreate) -> User:
    try:
        user = await User.create(
            telegram_id=user_create.telegram_id,
            username=user_create.username,
            first_name=user_create.first_name,
            last_name=user_create.last_name,
        )
        log.info("User created: %s", user.id)
        return user
    except IntegrityError as e:
        log.error("Failed to create user: %s", e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists.",
        )


async def get_user_by_telegram_id(telegram_id: int) -> User:
    try:
        user = await User.get(telegram_id=telegram_id)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )


async def update_user_birth_date_field(user_update: UserUpdate) -> User:
    user = await get_user_by_telegram_id(telegram_id=user_update.telegram_id)
    user.birth_date = user_update.birth_date

    try:
        await user.save()
        return user
    except IntegrityError:
        log.error("Invalid birth_date for user %s", user.id)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid birth_date format."
        )
