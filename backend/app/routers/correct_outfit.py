
from fastapi import APIRouter
from app.schemas.outfit import CorrectOutfitRequest

router = APIRouter(
    prefix="/correct-outfit",
    tags=["Correct My Outfit"]
)


@router.post("/analyze")
def analyze_outfit(request: CorrectOutfitRequest):
    return {
        "module": "Correct My Outfit",
        "message": "Your outfit analysis request was received.",
        "image_reference": request.image_reference,
        "occasion": request.occasion,
        "preferred_style": request.preferred_style,
        "status": "received"
    }