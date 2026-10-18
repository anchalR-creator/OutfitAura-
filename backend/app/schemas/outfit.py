
from pydantic import BaseModel, Field


# MODULE 1: CORRECT MY OUTFIT
class CorrectOutfitRequest(BaseModel):
    image_reference: str = Field(
        ...,
        description="Reference to the outfit image provided by the user"
    )

    occasion: str | None = None
    preferred_style: str | None = None


# MODULE 2: CREATE MY OUTFIT
class CreateOutfitRequest(BaseModel):
    body_type: str
    skin_tone: str
    height: str
    occasion: str
    style: str
    preferred_colors: list[str] = Field(default_factory=list)
    mood: str | None = None


# MODULE 3: AURAMATCH
class AuraMatchRequest(BaseModel):
    desired_style_reference: str
    wardrobe_items: list[str] = Field(default_factory=list)
    occasion: str | None = None