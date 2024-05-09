from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='./.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore',
        env_prefix='database_'
    )

    host: str
    port: int

    @property
    def url(self) -> str:
        return f'mongodb://{self.host}:{self.port}/'


class Settings(BaseSettings):
    db: DatabaseSettings

    @staticmethod
    def root_dir() -> Path:
        return Path(__file__).resolve().parent.parent.parent


def load_settings(
        database_settings: Optional[DatabaseSettings] = None
) -> Settings:
    return Settings(
        db=database_settings or DatabaseSettings()  # type: ignore[call-arg]
    )
