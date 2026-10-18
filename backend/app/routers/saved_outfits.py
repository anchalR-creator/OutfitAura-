
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, SavedOutfit
from app.schemas.saved_outfit import (
    SavedOutfitCreate,
    SavedOutfitResponse,
)

router = APIRouter(
    prefix="/saved-outfits",
    tags=["Saved Outfits"]
)


@router.post("/", response_model=SavedOutfitResponse, status_code=201)
def save_outfit(
    request: SavedOutfitCreate,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(
        User.id == request.user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    outfit = SavedOutfit(**request.model_dump())
    db.add(outfit)
    db.commit()
    db.refresh(outfit)

    return outfit


@router.get("/user/{user_id}", response_model=list[SavedOutfitResponse])
def get_saved_outfits(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return db.query(SavedOutfit).filter(
        SavedOutfit.user_id == user_id
    ).all()
