from fastapi import FastAPI

from backend.api.image import router as image_router

app = FastAPI(
    title="HLRegion AI",
    description="AI Platform for HL Region",
    version="1.0.0"
)

app.include_router(
    image_router,
    prefix="/api/v1",
    tags=["Image"]
)


@app.get("/")
def root():
    return {
        "status": "running",
        "project": "HLRegion AI"
    }