from pydantic import BaseModel, ConfigDict, Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=4)
    full_name: str | None = None


class UserOut(BaseModel):
    id: int
    username: str
    full_name: str | None = None

    model_config = ConfigDict(from_attributes=True)
