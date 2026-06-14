from fastapi import APIRouter
import os
from .schemas import VersionDTO

router = APIRouter(prefix="/api/v1/version", tags=["version"])

@router.get("/version", response_model=VersionDTO)
def get_version():
    return {
        "version": os.getenv("APP_VERSION", "0.0.0"),
        "environment": os.getenv("APP_ENVIRONMENT", "development")
    }