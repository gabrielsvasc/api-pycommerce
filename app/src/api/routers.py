from fastapi import APIRouter
from controller import (
    user_type,
)


main_router = APIRouter()
main_router.include_router(user_type.router)
