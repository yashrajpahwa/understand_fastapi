from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.cache import clear_cache, get_cache, set_cache
from app.db import crud
from app.db.session import get_db
from app.deps import get_current_user
from app.pagination import paginate
from app.schemas.items import ItemCreate, ItemOut, PaginatedItems

router = APIRouter(prefix="/items", tags=["items"])


@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED)
async def create_item(
    payload: ItemCreate,
    db: AsyncSession = Depends(get_db),
    user=Depends(get_current_user),
) -> ItemOut:
    item = await crud.create_item(db, user.id, payload.title, payload.description)
    clear_cache()
    return item


@router.get("", response_model=PaginatedItems)
async def list_items(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
) -> PaginatedItems:
    cache_key = f"items:{skip}:{limit}"
    cached = get_cache(cache_key)
    if cached:
        return cached
    items = await crud.list_items(db, skip=skip, limit=limit)
    total = await crud.count_items(db)
    payload = paginate(items, total, skip, limit)
    set_cache(cache_key, payload, ttl=10)
    return payload


@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)) -> ItemOut:
    item = await crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item
