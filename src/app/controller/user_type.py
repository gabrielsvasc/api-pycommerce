from fastapi import Depends
from typing import Annotated
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from service import UserTypeService as Service


router = APIRouter(prefix='/user_type')


@router.post("/")
def create_user_type(
    type_name: str,
    service: Annotated[Service, Depends(Service)]
) -> JSONResponse:
    if service.user_type_exists(type_name):
        return JSONResponse('Type name alredy exist!', 400)

    user_type = service.create_user_type(type_name)

    return JSONResponse(jsonable_encoder(user_type), 201)


@router.get("/")
def get_user_types(
    service: Annotated[Service, Depends(Service)]
) -> JSONResponse:
    user_types = service.list_user_types()

    return JSONResponse(jsonable_encoder(user_types), 200)
