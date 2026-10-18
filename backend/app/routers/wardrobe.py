
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User, WardrobeItem
from app.schemas.wardrobe import (
    WardrobeItemCreate,
    WardrobeItemResponse,
)

router = APIRouter(prefix="/wardrobe", tags=["Wardrobe"])


@router.post("/", response_model=WardrobeItemResponse, status_code=201)
def add_wardrobe_item(
    request: WardrobeItemCreate,
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

    item_data = request.model_dump()
    item = WardrobeItem(**item_data)

    db.add(item)
    db.commit()
    db.refresh(item)

    return item


@router.get("/user/{user_id}", response_model=list[WardrobeItemResponse])
def get_user_wardrobe(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return db.query(WardrobeItem).filter(
        WardrobeItem.user_id == user_id
    ).all()


@router.delete("/{item_id}", status_code=204)
def delete_wardrobe_item(
    item_id: int,
    db: Session = Depends(get_db),
):
    item = db.query(WardrobeItem).filter(
        WardrobeItem.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Wardrobe item not found"
        )

    db.delete(item)
    db.commit()

    return None

@router.put("/{item_id}")
def update_wardrobe_item(
    item_id: int,
    request: WardrobeItemCreate,
    db: Session = Depends(get_db),
):
    item = db.query(WardrobeItem).filter(
        WardrobeItem.id == item_id
    ).first()

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Wardrobe item not found"
        )

    item.name = request.name
    item.category = request.category
    item.color = request.color

    db.commit()
    db.refresh(item)

    return item