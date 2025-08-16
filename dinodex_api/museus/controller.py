from fastapi  import APIRouter, Body, HTTPException, status
from uuid     import uuid4
from pydantic import UUID4

from sqlalchemy.future import select

from dinodex_api.contrib.dependencies import DatabaseDependency
from dinodex_api.museus.schemas       import MuseuIn, MuseuOut
from dinodex_api.museus.models        import MuseuModel

router = APIRouter()

@router.post(
        "/", 
        summary        = "Cadastrar um novo museu",
        status_code    = status.HTTP_201_CREATED,
        response_model = MuseuOut,
)
async def post(
    db_session : DatabaseDependency,
    museu_in   : MuseuIn = Body(...)
) -> MuseuOut:
    
    museu_out   = MuseuOut(id=uuid4(), **museu_in.model_dump(),)
    museu_model = MuseuModel(**museu_out.model_dump())

    db_session.add(museu_model)
    await db_session.commit()

    return museu_out


@router.get(
        "/", 
        summary        = "Consultar todos os museus",
        status_code    = status.HTTP_200_OK,
        response_model = list[MuseuOut],
)
async def query(
    db_session: DatabaseDependency,
) -> list[MuseuOut]:
    
    museus: list[MuseuOut] = (await db_session.execute(select(MuseuModel))).scalars().all()
    
    return museus


@router.get(
        "/{id}", 
        summary        = "Consultar um museu pelo ID ",
        status_code    = status.HTTP_200_OK,
        response_model = MuseuOut,
)
async def query(
    id         : UUID4,
    db_session : DatabaseDependency,
) -> MuseuOut:
    
    museu: MuseuOut = (
        await db_session.execute(select(MuseuModel).filter_by(id=id))
    ).scalars().first()
    
    if not museu:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail      = f"Museu não encontrado pelo ID: {id}"
        )

    return museu
