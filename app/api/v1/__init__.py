from fastapi import APIRouter

from .auth import router, authrouter
from .smtp_service import router as smtp_router

route = APIRouter(prefix="/v1")

route.include_router(router)
route.include_router(authrouter)
route.include_router(smtp_router)

__all__ = [route]
