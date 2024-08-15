import os
from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES = os.path.join(BASE_DIR, "templates")


class Settings(BaseSettings):
    """Класс для настроек проекта, хранения и валидации переменных окружения"""

    API_TOKEN: str
    SECRET_KEY: str
    HOST: str
    PORT: str

    class Config:
        env_file = ".env"


settings = Settings()
