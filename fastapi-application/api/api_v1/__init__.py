from fastapi import APIRouter

from core.config import settings
from .api_v1_donuts import router as donuts_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    donuts_router,
    prefix=settings.api.v1.donuts,
)
