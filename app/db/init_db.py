from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from app.db.base import Base
from app.db import crud, models


async def init_db(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def seed_data(session: AsyncSession) -> None:
    result = await session.execute(select(models.User).limit(1))
    if result.scalar_one_or_none() is None:
        user = await crud.create_user(session, "demo", "demo", "Demo User")
        await crud.create_item(session, user.id, "First item", "Seeded item")
