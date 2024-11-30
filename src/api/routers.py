from fastapi import APIRouter

from api.status import STATUS_ROUTER

ROUTER = APIRouter(prefix='/v1')
ROUTER.include_router(STATUS_ROUTER)
