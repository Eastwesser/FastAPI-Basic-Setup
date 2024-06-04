from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.user import UserRead
from crud.users import get_all_users

router = APIRouter(tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(
        session: AsyncSession = Depends(db_helper.session_getter),
):
    users = await get_all_users(session=session)
    return users
