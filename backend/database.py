import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]
# 형식: postgresql+psycopg://{user}:{password}@{host}:{port}/{db}
# 예:   postgresql+psycopg://contact_app:{password}@localhost:5432/contact_app
# 배포 플랫폼(Render 등)이 제공하는 DATABASE_URL은 드라이버 접두사 없는
# "postgresql://"만 줄 수 있다 — psycopg3를 쓰도록 여기서 보정한다.
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
