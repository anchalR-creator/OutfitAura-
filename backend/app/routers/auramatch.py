
from fastapi import APIRouter
from app.schemas.outfit import AuraMatchRequest

router = APIRouter(
    prefix="/auramatch",
    tags=["AuraMatch - AI Style Gap Analyzer"]
)


@router.post("/analyze")
def analyze_style_gap(request: AuraMatchRequest):
    return {
        "module": "AuraMatch",
        "message": "Your style gap analysis request was received.",
        "desired_style_reference": request.desired_style_reference,
        "wardrobe_items": request.wardrobe_items,
        "occasion": request.occasion,
        "status": "received"
    }