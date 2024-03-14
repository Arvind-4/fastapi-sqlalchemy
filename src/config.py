from pydantic import Field
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    FASTAPI_DATABASE_URL: str = Field(..., env="FASTAPI_DATABASE_URL")
    FASTAPI_DATABASE_AUTH_TOKEN: str = Field(..., env="FASTAPI_DATABASE_AUTH_TOKEN")

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()