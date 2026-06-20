# db/session.py — Database engine, session factory, and get_db dependency
# Module: IB Wallet (Pots) | Task: IBBUD-11

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

DATABASE_URL = "sqlite:///./ib_wallet.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite only — remove this line for Postgres/MariaDB
    echo=False,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator:
    """
    FastAPI dependency. Yields a DB session and closes it after the request.
    Usage: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
