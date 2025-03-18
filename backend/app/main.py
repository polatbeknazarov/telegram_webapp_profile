import logging
import uvicorn

from core.config import settings
from create_fastapi_app import create_app
from api import router as api_router

logging.basicConfig(
    level=settings.logging.log_level_value,
    format=settings.logging.log_format,
)

main_app = create_app()
main_app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host="localhost",
        port=8000,
        reload=True,
    )
