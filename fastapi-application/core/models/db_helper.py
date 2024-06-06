import os
from typing import AsyncGenerator

from alembic import command
from alembic.config import Config
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)

from core.config import settings
from core.models.base import Base  # Import Base from its module

load_dotenv()


class DatabaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            echo_pool: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def connect(self) -> None:
        alembic_ini_path = os.getenv("ALEMBIC_INI_PATH")
        if not alembic_ini_path:
            raise ValueError("ALEMBIC_INI_PATH environment variable not set")

        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

            alembic_cfg = Config(alembic_ini_path)
            command.upgrade(alembic_cfg, "head")

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)
