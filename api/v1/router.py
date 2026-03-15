from fastapi import APIRouter

from api.v1.query_router import router as query_router
from api.v1.auth_router import router as auth_router

router = APIRouter()

router.include_router(
    query_router
)

router.include_router(
    auth_router,
)