
from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey, DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    body_type = Column(String(50), nullable=True)
    skin_tone = Column(String(50), nullable=True)
    height = Column(String(30), nullable=True)

    wardrobe_items = relationship(
        "WardrobeItem",
        back_populates="owner",
        cascade="all, delete-orphan"
    )

    saved_outfits = relationship(
        "SavedOutfit",
        back_populates="owner",
        cascade="all, delete-orphan"
    )


class WardrobeItem(Base):
    __tablename__ = "wardrobe_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    category = Column(String(100), nullable=True)
    color = Column(String(50), nullable=True)
    image_reference = Column(String(500), nullable=True)

    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    owner = relationship("User", back_populates="wardrobe_items")


class SavedOutfit(Base):
    __tablename__ = "saved_outfits"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    outfit_data = Column(Text, nullable=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now()
    )

    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=False
    )

    owner = relationship("User", back_populates="saved_outfits")
