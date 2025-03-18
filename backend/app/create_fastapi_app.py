import logging

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from core.config import settings
from bot.create_bot import bot, dp
from core.setup_db import init_db_tortoise

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    log.info("Starting application lifespan...")

    try:
        log.info("Initializing database...")
        await init_db_tortoise(app=app)
        log.info("Database initialized successfully")
    except Exception as e:
        log.exception("Failed to initialize the database: %s", e)

    try:
        log.info("Setting up bot webhook...")
        await bot.set_webhook(
            url=settings.bot.webhook_url,
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True,
        )
        log.info("Webhook set successfully")
    except Exception as e:
        log.exception("Failed to set webhook: %s", e)

    yield

    try:
        log.info("Closing database connections...")
        await Tortoise.close_connections()
        log.info("Database connections closed successfully")
    except Exception as e:
        log.exception("Error while closing database connections: %s", e)

    log.info("Application lifespan completed")


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
