
from fastapi import APIRouter
from app.schemas.outfit import CreateOutfitRequest

router = APIRouter(
    prefix="/create-outfit",
    tags=["Create My Outfit"]
)


@router.post("/generate")
def generate_outfit(request: CreateOutfitRequest):
    return {
        "module": "Create My Outfit",
        "message": "Your outfit creation request was received.",
        "body_type": request.body_type,
        "skin_tone": request.skin_tone,
        "height": request.height,
        "occasion": request.occasion,
        "style": request.style,
        "preferred_colors": request.preferred_colors,
        "mood": request.mood,
        "status": "received"
    }