import logging

from typing import Literal
from pathlib import Path

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent
LOG_DEFAULT_FORMAT = (
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)


class LoggingConfig(BaseModel):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]


class BotConfig(BaseModel):
    token: str
    web_app_url: str
    webhook_url: str


class APIV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    webhook: str = "/webhook"


class APIPrefix(BaseModel):
    prefix: str = "/api"
    v1: APIV1Prefix = APIV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    logging: LoggingConfig = LoggingConfig()
    bot: BotConfig
    db: DatabaseConfig
    api: APIPrefix = APIPrefix()


settings = Settings()
