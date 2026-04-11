from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from typing import List
import cloudinary
import cloudinary.uploader
from database import db
from datetime import datetime
from routes.auth import verify_token
from services.blur_detection import detect_blur
from services.duplicate_detection import check_duplicate
from services.technical_quality import analyze_technical_quality
from services.clipiqa_scorer import predict_aesthetic_score
from services.explainability import generate_explanation

router = APIRouter()

@router.post("/upload")
async def upload_images(
    file: UploadFile = File(...),
    current_user: dict = Depends(verify_token)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail=f"{file.filename} is not an image!")

    contents = await file.read()

    blur_result = detect_blur(contents)
    technical_result = analyze_technical_quality(contents)
    aesthetic_result = predict_aesthetic_score(contents)

    existing_hashes = list(db.images.find(
        {"user_email": current_user["email"]},
        {"filename": 1, "phash": 1, "_id": 0}
    ))
    duplicate_result = check_duplicate(contents, existing_hashes)

    # Generate explanation
    explanation = generate_explanation({
        "sharpness": technical_result["sharpness"],
        "exposure_accuracy": technical_result["exposure_accuracy"],
        "noise_control": technical_result["noise_control"],
        "saturation_balance": technical_result["saturation_balance"],
        "contrast_quality": technical_result["contrast_quality"],
        "technical_score": technical_result["technical_score"],
        "aesthetic_score": aesthetic_result["aesthetic_score"]
    })

    result = cloudinary.uploader.upload(
        contents,
        folder="picpicky/uploads",
        resource_type="image"
    )

    image_doc = {
        "user_email": current_user["email"],
        "filename": file.filename,
        "cloudinary_url": result["secure_url"],
        "cloudinary_id": result["public_id"],
        "uploaded_at": datetime.utcnow(),
        "status": "uploaded",
        "blur_score": blur_result["blur_score"],
        "is_blurry": blur_result["is_blurry"],
        "phash": duplicate_result["phash"],
        "is_duplicate": duplicate_result["is_duplicate"],
        "duplicate_of": duplicate_result["duplicate_of"],
        "sharpness": technical_result["sharpness"],
        "exposure_accuracy": technical_result["exposure_accuracy"],
        "noise_control": technical_result["noise_control"],
        "saturation_balance": technical_result["saturation_balance"],
        "contrast_quality": technical_result["contrast_quality"],
        "technical_score": technical_result["technical_score"],
        "aesthetic_score": aesthetic_result["aesthetic_score"],
        "aesthetic_label": aesthetic_result["aesthetic_label"],
        "verdict": explanation["verdict"],
        "strengths": explanation["strengths"],
        "issues": explanation["issues"],
        "suggestions": explanation["suggestions"]
    }

    db.images.insert_one(image_doc)

    return {
        "message": "Image uploaded successfully!",
        "filename": file.filename,
        "url": result["secure_url"],
        "blur_score": blur_result["blur_score"],
        "is_blurry": blur_result["is_blurry"],
        "is_duplicate": duplicate_result["is_duplicate"],
        "duplicate_of": duplicate_result["duplicate_of"],
        "technical_score": technical_result["technical_score"],
        "sharpness": technical_result["sharpness"],
        "exposure_accuracy": technical_result["exposure_accuracy"],
        "noise_control": technical_result["noise_control"],
        "saturation_balance": technical_result["saturation_balance"],
        "contrast_quality": technical_result["contrast_quality"],
        "aesthetic_score": aesthetic_result["aesthetic_score"],
        "aesthetic_label": aesthetic_result["aesthetic_label"],
        "verdict": explanation["verdict"],
        "strengths": explanation["strengths"],
        "issues": explanation["issues"],
        "suggestions": explanation["suggestions"]
    }