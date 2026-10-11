from fastapi import FastAPI
from python_pos_system.core.settings import settings
from python_pos_system.core.database import engine, Base
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    lifespan=lifespan
)

@app.get("/", tags=["DEFAULT"])
async def root():
    return {"message": "Welcome to the POS system API"}

@app.get("/health", tags=["DEFAULT"])
async def health():
    return {"status": "OK"}