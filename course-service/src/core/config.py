"""Application configuration."""

import functools
from typing import final

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application settings."""

    title: str = "Course service title"
    description: str = "Course service description"
    summary: str = "Course service summary"

    host: str
    port: int
    log_level: str


@final
class Settings(BaseSettings):
    """Course service settings."""

    app: AppSettings
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
    )


@functools.lru_cache
def get_settings() -> Settings:
    """Return cached application settings."""
    return Settings()  # type: ignore[call-arg]
