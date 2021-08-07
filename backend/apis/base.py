from fastapi import APIRouter

from apis.version1 import route_uesrs

api_router = APIRouter()

api_router.include_router(route_uesrs.router, prefix="/user", tags=["users"])
