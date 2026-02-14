from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import security
from app.db import models


async def get_user_by_username(session: AsyncSession, username: str):
    result = await session.execute(
        select(models.User).where(models.User.username == username)
    )
    return result.scalar_one_or_none()


async def list_users(session: AsyncSession):
    result = await session.execute(select(models.User))
    return result.scalars().all()


async def create_user(
    session: AsyncSession, username: str, password: str, full_name: str | None = None
):
    user = models.User(
        username=username,
        hashed_password=security.get_password_hash(password),
        full_name=full_name,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def authenticate_user(session: AsyncSession, username: str, password: str):
    user = await get_user_by_username(session, username)
    if not user or not security.verify_password(password, user.hashed_password):
        return None
    return user


async def create_item(
    session: AsyncSession, owner_id: int, title: str, description: str | None = None
):
    item = models.Item(title=title, description=description, owner_id=owner_id)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item


async def list_items(session: AsyncSession, skip: int = 0, limit: int = 10):
    result = await session.execute(select(models.Item).offset(skip).limit(limit))
    return result.scalars().all()


async def count_items(session: AsyncSession) -> int:
    result = await session.execute(select(func.count()).select_from(models.Item))
    return int(result.scalar_one())


async def get_item(session: AsyncSession, item_id: int):
    result = await session.execute(select(models.Item).where(models.Item.id == item_id))
    return result.scalar_one_or_none()
