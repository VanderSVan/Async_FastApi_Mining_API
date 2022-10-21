from pathlib import Path
from functools import lru_cache

from pydantic import BaseSettings, Field

# Paths:
api_dir = Path(__file__).parent
project_dir = api_dir.parent


class Settings(BaseSettings):
    # Database:
    PG_SUPER_DB: str = Field(..., env='PG_SUPER_DB')
    PG_SUPER_USER: str = Field(..., env='PG_SUPER_USER')
    PG_SUPER_PASSWORD: str = Field(..., env='PG_SUPER_PASSWORD')
    PG_HOST: str = Field(..., env='PG_HOST')
    PG_PORT: str = Field(..., env='PG_PORT')
    PG_USER_DB: str = Field(..., env='PG_USER_DB')
    PG_USER: str = Field(..., env='PG_USER')
    PG_USER_PASSWORD: str = Field(..., env='PG_USER_PASSWORD')
    PG_ROLE: str = Field(None, env='PG_ROLE')

    # Security:
    # To generate a secure random secret key use the command in your terminal:
    # `openssl rand -hex 32`.
    SECRET_KEY: str = Field(..., env='SECRET_KEY')
    ALGORITHM: str = "HS256"
    TIME_ZONE: str = 'Europe/Moscow'
    ACCESS_TOKEN_EXPIRE_MINUTES = 120

    class Config:
        env_file = project_dir.joinpath(".env")
        env_file_encoding = 'utf-8'

    def get_database_url(self) -> str:
        """
        Gets the full path to the database.
        :return: URL string.
        """
        return (
            f'postgresql+asyncpg://'
            f'{self.PG_USER}:'
            f'{self.PG_USER_PASSWORD}@'
            f'{self.PG_HOST}:'
            f'{self.PG_PORT}/'
            f'{self.PG_USER_DB}'
        )


@lru_cache()
def get_settings() -> Settings:
    """Gets cached settings."""
    return Settings()
