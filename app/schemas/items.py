from pydantic import BaseModel, ConfigDict, Field


class ItemCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str | None = None


class ItemOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class PaginatedItems(BaseModel):
    items: list[ItemOut]
    total: int
    skip: int
    limit: int
