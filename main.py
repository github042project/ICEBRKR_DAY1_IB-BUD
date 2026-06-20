# main.py — IB Wallet (Pots) FastAPI application entry point
# Module: IB Wallet (Pots) | Task: IBBUD-11

from fastapi import FastAPI
from sqlalchemy import text
from db.session import engine, DATABASE_URL
from db.base import Base
from money import Money

# Import all models so Base.metadata knows about them
import models.wallet_meta  # noqa: F401

# ─────────────────────────────────────────────
# APP
# ─────────────────────────────────────────────

app = FastAPI(
    title="IB Wallet",
    description="IB Bud — Wallet (Pots) service. IBBUD-11.",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup():
    """Create all tables on startup if they do not exist yet."""
    Base.metadata.create_all(bind=engine)


# ─────────────────────────────────────────────
# HEALTH CHECK
# ─────────────────────────────────────────────

@app.get("/health", tags=["System"])
def health_check():
    """
    Health check endpoint.
    Confirms the app is running and the database is reachable.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "status": "ok" if db_status == "ok" else "degraded",
        "service": "ib-wallet",
        "module": "IB Bud - Wallet (Pots)",
        "task": "IBBUD-11",
        "db": db_status,
    }


# ─────────────────────────────────────────────
# DEV ENDPOINT — REMOVE BEFORE PRODUCTION
# ─────────────────────────────────────────────

@app.get("/dev/money-check", tags=["Dev"])
def money_check():
    """
    Sanity check for the Money type.
    REMOVE THIS ENDPOINT BEFORE PRODUCTION.
    """
    a = Money("1000.00", "INR")
    b = Money("250.50", "INR")
    result = a - b

    return {
        "a": a.to_dict(),
        "b": b.to_dict(),
        "a_minus_b": result.to_dict(),
        "note": "If amount is 749.50 INR, Decimal math is working correctly.",
    }
