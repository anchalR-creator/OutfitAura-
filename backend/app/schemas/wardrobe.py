
from pydantic import BaseModel, ConfigDict


class WardrobeItemCreate(BaseModel):
    name: str
    category: str | None = None
    color: str | None = None
    image_reference: str | None = None
    user_id: int


class WardrobeItemResponse(BaseModel):
    id: int
    name: str
    category: str | None = None
    color: str | None = None
    image_reference: str | None = None
    user_id: int

    model_config = ConfigDict(from_attributes=True)
