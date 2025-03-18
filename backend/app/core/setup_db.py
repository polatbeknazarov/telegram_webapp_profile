import logging

from fastapi import FastAPI
from tortoise import Tortoise

from core.config import settings

log = logging.getLogger(__name__)


async def init_db_tortoise(app: FastAPI):
    try:
        await Tortoise.init(
            db_url=str(settings.db.url),
            modules={"models": ["core.models"]},
        )
        await Tortoise.generate_schemas()
    except Exception as e:
        raise e
