from typing import Sequence

from core.schemas.schemas_donut import DonutCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Donut


async def get_all_donuts(
        session: AsyncSession,
) -> Sequence[Donut]:
    stmt = select(Donut).order_by(Donut.id)
    result = await session.execute(stmt)
    return result.scalars().all()


async def create_donut(
        session: AsyncSession,
        donut_create: DonutCreate,
) -> Donut:
    donut = Donut(**donut_create.model_dump())
    session.add(donut)
    await session.commit()
    return donut
