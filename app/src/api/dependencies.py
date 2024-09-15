from core.database import create_session
from sqlalchemy.orm import Session
from typing import Generator, Any


def get_db_session() -> Generator[Session, Any, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.close()
