from core import settings
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy.engine import create_engine


DB_URL = URL.create(
    drivername=settings.DB_ENGINE,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    database=settings.DB_NAME,
    port=settings.DB_PORT
)
ENGINE = create_engine(DB_URL)


class Base(DeclarativeBase):
    pass


def create_session() -> Session:
    return Session(bind=ENGINE, autoflush=False)
