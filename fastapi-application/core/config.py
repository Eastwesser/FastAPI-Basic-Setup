import os

from dotenv import load_dotenv
from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings

load_dotenv()


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    donuts: str = "/donuts"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    naming_convention: dict = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }


class Settings(BaseSettings):
    class Config:
        extra = 'forbid'

    alembic_ini_path: str = os.getenv("ALEMBIC_INI_PATH", "default_value.ini")  # Provide a default value
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig(url=os.getenv("DB_URL"))  # type: ignore # Use os.getenv directly


settings = Settings()
