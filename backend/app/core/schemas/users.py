from datetime import date, datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    telegram_id: int
    username: str | None = None
    first_name: str | None = None
    last_name: str | None


class UserRead(UserBase):
    id: int
    birth_date: date | None = None
    created_at: datetime
    updated_at: datetime


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    telegram_id: int
    birth_date: date
