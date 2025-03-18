from fastapi import APIRouter

from core.config import settings
from .v1 import api_v1_router

router = APIRouter(prefix=settings.api.prefix)
router.include_router(api_v1_router)
