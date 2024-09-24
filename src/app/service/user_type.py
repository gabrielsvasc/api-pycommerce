from typing import List
from fastapi import Depends
from typing import Annotated
from schema import UserTypeResponse
from app.src.utils.string_formatter import standardize_text
from repository import UserTypeRepository as Repository


class UserTypeService:
    def __init__(self, repository: Annotated[Repository, Depends(Repository)]):
        self.repository = repository

    def user_type_exists(self, type_name: str) -> bool:
        unique_name = standardize_text(type_name)

        return self.repository \
            .record_exists(unique_name)

    def create_user_type(self, type_name: str) -> UserTypeResponse:
        unique_name = standardize_text(type_name)

        user_type_orm = self.repository \
            .insert_user_type(unique_name)

        return UserTypeResponse.model_validate(user_type_orm)

    def list_user_types(self) -> List[UserTypeResponse]:
        user_types_orm = self.repository.select_all_user_types()

        return [UserTypeResponse.model_validate(orm) for orm in user_types_orm]
