from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import get_settings

settings = get_settings()

SQLALCHEMY_DATABASE_URL = f"sqlite+{settings.FASTAPI_DATABASE_URL}/?authToken={settings.FASTAPI_DATABASE_AUTH_TOKEN}&secure=true"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
