from fastapi import APIRouter, Body, status

from dinodex_api.contrib.dependencies import DatabaseDependency
from dinodex_api.especime.schemas     import EspecimeIn

router = APIRouter()

@router.post(
        "/", 
        summary="Catalogar novo espécime.",
        status_code=status.HTTP_201_CREATED,
)
async def post(
    db_session: DatabaseDependency,
    especime_in: EspecimeIn = Body(...)
):
    pass