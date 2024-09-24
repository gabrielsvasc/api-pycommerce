from core.database import Base
from sqlalchemy.orm import (
    Mapped as Map,
    mapped_column,
)


class UserType(Base):
    __tablename__ = "user_type"

    type_id: Map[int] = mapped_column(primary_key=True, autoincrement=True)
    type_name: Map[str] = mapped_column(primary_key=True)
