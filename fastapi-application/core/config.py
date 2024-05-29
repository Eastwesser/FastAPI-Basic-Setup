import os

from dotenv import load_dotenv
from pydantic import (
    BaseModel,
    PostgresDsn,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

load_dotenv()


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


db_url = os.getenv("FASTAPI_CONFIG__DB__URL")


class DatabaseConfig(BaseModel):
    url: PostgresDsn = db_url
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env-template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
