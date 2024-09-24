from typing import List
from model import UserType
from fastapi import Depends
from typing import Annotated
from sqlalchemy import exists, select
from sqlalchemy.orm import Session
from api.dependencies import get_db_session


class UserTypeRepository:
    def __init__(
            self,
            session: Annotated[Session, Depends(get_db_session)]
    ) -> None:
        self.session = session

    def record_exists(self, type_name: str) -> bool:
        return self.session.query(
            exists().where(UserType.type_name == type_name)
        ).scalar()

    def insert_user_type(self, type_name: str) -> UserType:
        user_types_orm = UserType(type_name=type_name)

        self.session.add(user_types_orm)
        self.session.commit()
        self.session.refresh(user_types_orm)

        return user_types_orm

    def select_all_user_types(self) -> List[UserType]:
        return self.session \
            .scalars(select(UserType)) \
            .all()
