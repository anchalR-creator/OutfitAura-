
from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    username: str
    email: str
    body_type: str | None = None
    skin_tone: str | None = None
    height: str | None = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    body_type: str | None = None
    skin_tone: str | None = None
    height: str | None = None

    model_config = ConfigDict(from_attributes=True)
