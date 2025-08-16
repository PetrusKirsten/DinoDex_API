from fastapi import APIRouter

from dinodex_api.especime.controller import router as especime
from dinodex_api.taxons.controller import router as taxons

api_router = APIRouter()
api_router.include_router(especime, prefix='/especimes', tags=['especimes'])
api_router.include_router(taxons, prefix='/taxons', tags=['taxons'])
