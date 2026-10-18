from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app import models
from app.routers import correct_outfit, create_outfit, auramatch, users, wardrobe, saved_outfits
from pathlib import Path
from uuid import uuid4


# Create database tables
Base.metadata.create_all(bind=engine)

UPLOAD_DIR = Path(__file__).resolve().parent / "app" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app = FastAPI(
    title="OutfitAura API",
    description="Backend API for the OutfitAura AI fashion assistant",
    version="0.1.0"
)

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the OutfitAura backend!",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "OutfitAura"
    }


# Register the three modules
app.include_router(correct_outfit.router)
app.include_router(create_outfit.router)
app.include_router(auramatch.router)
app.include_router(users.router)
app.include_router(wardrobe.router)
app.include_router(saved_outfits.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8081",
        "http://127.0.0.1:8081",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image file."
        )

    contents = await file.read()

    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="Image must be smaller than 10 MB."
        )

    extension = {
        "image/jpeg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
    }.get(file.content_type)

    if extension is None:
        raise HTTPException(
            status_code=400,
            detail="Only JPG, PNG, WEBP, and GIF images are supported."
        )

    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename
    file_path.write_bytes(contents)

    return {
        "image_url": f"http://127.0.0.1:8000/uploads/{filename}"
    }