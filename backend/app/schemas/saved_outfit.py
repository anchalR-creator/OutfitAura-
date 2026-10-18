
from pydantic import BaseModel, ConfigDict


class SavedOutfitCreate(BaseModel):
    title: str
    description: str | None = None
    outfit_data: str | None = None
    user_id: int


class SavedOutfitResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    outfit_data: str | None = None
    user_id: int

    model_config = ConfigDict(from_attributes=True)
