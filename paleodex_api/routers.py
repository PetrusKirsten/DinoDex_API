from fastapi import APIRouter

from paleodex_api.especime.controller import router as especime
from paleodex_api.taxons.controller import router as taxons
from paleodex_api.museus.controller import router as museus

api_router = APIRouter()

api_router.include_router(especime, prefix='/especimes', tags=['especimes'])
api_router.include_router(taxons,   prefix='/taxons',    tags=['taxons'])
api_router.include_router(museus,   prefix='/museus',    tags=['museus'])
