from fastapi import APIRouter
from dinodex_api.especime.controller import router as especime

api_router = APIRouter()
api_router.include_router(especime, prefix=['especimes'], tags=['especimes/'])
