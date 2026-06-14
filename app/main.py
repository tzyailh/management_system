from fastapi import FastAPI
from app.api.v1.router_user import router as user_router
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI + MySQL Project")

app.include_router(user_router, prefix="/api/v1")