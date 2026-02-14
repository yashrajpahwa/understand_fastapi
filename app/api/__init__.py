from fastapi import APIRouter

from app.api.routes import auth, basic, items, users, ws

api_router = APIRouter()
api_router.include_router(basic.router)
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(items.router)
api_router.include_router(ws.router)
