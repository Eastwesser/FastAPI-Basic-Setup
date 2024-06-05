from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Donut
from core.schemas.user import UserCreate


async def get_all_users(
        session: AsyncSession,
) -> Sequence[Donut]:
    stmt = select(Donut).order_by(Donut.id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def create_user(
        session: AsyncSession,
        user_create: UserCreate,
) -> Donut:
    user = Donut(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user
