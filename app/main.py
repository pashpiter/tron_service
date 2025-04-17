from fastapi import FastAPI

from core.config import settings
from api.endpoints import router


app = FastAPI(debug=settings.app.debug)
app.include_router(router)
