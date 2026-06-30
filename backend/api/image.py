from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

from backend.services.image_service import image_to_png

router = APIRouter()


@router.post("/image")
async def image(file: UploadFile = File(...)):
    return StreamingResponse(
        image_to_png(file),
        media_type="image/png"
    )