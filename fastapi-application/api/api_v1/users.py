from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.user import UserRead, UserCreate
from crud import users as crud_users

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
        # session: AsyncSession = Depends(db_helper.session_getter),
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ],
):
    users = await crud_users.get_all_users(session=session)
    return users


@router.post("", response_model=UserRead)
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter)
        ],
        user_create: UserCreate,
):
    user = await crud_users.create_user(
        session=session,
        user_create=user_create,
    )
    return user
