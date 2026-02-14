from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import api_router
from app.core.config import settings
from app.db.init_db import init_db, seed_data
from app.db.session import AsyncSessionLocal, engine
from app.middleware import TimingMiddleware
from app.openapi import custom_openapi

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TimingMiddleware)

app.include_router(api_router)


@app.on_event("startup")
async def on_startup() -> None:
    await init_db(engine)
    async with AsyncSessionLocal() as session:
        await seed_data(session)


app.openapi = lambda: custom_openapi(app)
