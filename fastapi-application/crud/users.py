from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Donut


async def get_all_users(
        session: AsyncSession,
) -> Sequence[Donut]:
    stmt = select(Donut).order_by(Donut.id)
    result = await session.execute(stmt)
    return result.scalars().all()
