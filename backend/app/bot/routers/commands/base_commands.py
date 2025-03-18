from aiogram import types, Router
from aiogram.types import WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.config import settings

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    markup = (
        InlineKeyboardBuilder()
        .button(
            text="Open Web App",
            web_app=WebAppInfo(url=settings.bot.web_app_url),
        )
        .as_markup()
    )
    await message.answer(
        text=f"Hello, {message.from_user.full_name}!",
        reply_markup=markup,
    )
