from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.endpoints import router
from core.config import settings
from database.create_table import create_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    yield

app = FastAPI(debug=settings.app.debug, lifespan=lifespan)
app.include_router(router)
