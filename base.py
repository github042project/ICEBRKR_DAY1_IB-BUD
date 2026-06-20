# db/base.py — SQLAlchemy DeclarativeBase
# Module: IB Wallet (Pots) | Task: IBBUD-11
# This is the ONLY place DeclarativeBase is imported. All models inherit from Base here.

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
