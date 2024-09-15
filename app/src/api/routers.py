from fastapi import APIRouter

API_ROUTERS = {
    "user_type": APIRouter(prefix="user_type", tags=["user_type"]),
}


def get_router(base_route: str) -> APIRouter:
    return API_ROUTERS.get(base_route)
