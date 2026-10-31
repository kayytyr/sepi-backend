from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import select

from app.database import SessionDep, engine
from app.models import Komoditas, KomoditasPublic

app = FastAPI(title="Sempol API")


@app.get("/health")
def health():
    """Cek apakah server hidup dan database bisa dihubungi."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        database = "ok"
    except SQLAlchemyError:
        database = "error"
    return {"status": "ok", "database": database}


@app.get("/komoditas", response_model=list[KomoditasPublic])
def daftar_komoditas(session: SessionDep):
    """Daftar semua komoditas, diurutkan berdasarkan nama."""
    return session.exec(select(Komoditas).order_by(Komoditas.nama)).all()
