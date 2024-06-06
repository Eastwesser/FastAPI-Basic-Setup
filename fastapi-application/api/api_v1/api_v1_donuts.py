from typing import Annotated

from core.schemas.schemas_donut import DonutRead, DonutCreate  # Изменено здесь
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from crud import donuts_crud as crud_donuts

router = APIRouter(tags=["Donuts"])


@router.get("", response_model=list[DonutRead])
async def get_donuts(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ],
):
    donuts = await crud_donuts.get_all_donuts(session=session)
    return donuts


@router.post("", response_model=DonutRead)
async def create_donut(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ],
        donut_create: DonutCreate,
):
    donut = await crud_donuts.create_donut(
        session=session,
        donut_create=donut_create,
    )
    return donut
