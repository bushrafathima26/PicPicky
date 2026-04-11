from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import cloudinary
from config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET
from database import db
from routes.auth import router as auth_router
from routes.upload import router as upload_router

app = FastAPI(
    title="Image Quality Assessment API",
    description="API for assessing image quality and photographer profiling",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

app.include_router(auth_router)

app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "Image Quality Assessment API is running!"}