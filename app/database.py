from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from app.config import settings

# Engine dibuat sekali untuk seluruh aplikasi.
# pool_pre_ping: cek dulu koneksi masih hidup sebelum dipakai,
# karena Neon menutup koneksi yang lama menganggur.
engine = create_engine(settings.database_url, pool_pre_ping=True)


def get_session():
    """Memberi satu Session per request, lalu menutupnya setelah request selesai."""
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
