from fastapi import APIRouter, Request
from aiogram.types import Update

from core.config import settings
from bot.create_bot import bot, dp

webhook_router = APIRouter(
    prefix=settings.api.v1.webhook,
    tags=["Webhook"],
)


@webhook_router.post("")
async def webhook(request: Request):
    update = Update.model_validate(
        await request.json(),
        context={"bot": bot},
    )
    await dp.feed_update(bot, update)
