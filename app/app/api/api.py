from fastapi import APIRouter

from app.api.endpoints.unit import router as assessments_router

api_router = APIRouter()
api_router.include_router(assessments_router, prefix="/units")
