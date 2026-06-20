# models/wallet_meta.py — Placeholder model to prove migrations work
# Module: IB Wallet (Pots) | Task: IBBUD-11

from datetime import datetime
from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base


class WalletMeta(Base):
    __tablename__ = "wallet_meta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
