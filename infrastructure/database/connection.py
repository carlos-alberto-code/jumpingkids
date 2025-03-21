import os
from dotenv import load_dotenv

from typing import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

load_dotenv()

DATABASE_URL_PRE = os.getenv("DATABASE_URL_PRE", "sqlite:///:memory:")

engine = create_engine(DATABASE_URL_PRE, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Generador de sesión para la base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
