from fastapi  import APIRouter, Body, HTTPException, status
from uuid     import uuid4
from pydantic import UUID4

from sqlalchemy.future import select

from dinodex_api.contrib.dependencies import DatabaseDependency
from dinodex_api.museu.schemas       import MuseuIn, MuseuOut
from dinodex_api.museu.models        import MuseuModel

router = APIRouter()

@router.post(
        "/", 
        summary="Cadastrar um novo museu",
        status_code=status.HTTP_201_CREATED,
        response_model=TaxonOut,
)
async def post(
    db_session: DatabaseDependency,
    taxon_in: TaxonIn = Body(...)
) -> TaxonOut:
    
    taxon_out = TaxonOut(id=uuid4(), **taxon_in.model_dump(),)
    taxon_model = TaxonModel(**taxon_out.model_dump())

    db_session.add(taxon_model)
    await db_session.commit()

    return taxon_out


@router.get(
        "/", 
        summary="Consultar todos os taxons",
        status_code=status.HTTP_200_OK,
        response_model=list[TaxonOut],
)
async def query(
    db_session: DatabaseDependency,
) -> list[TaxonOut]:
    
    taxons: list[TaxonOut] = (await db_session.execute(select(TaxonModel))).scalars().all()
    
    return taxons


@router.get(
        "/{id}", 
        summary="Consultar um taxon pelo ID ",
        status_code=status.HTTP_200_OK,
        response_model=TaxonOut,
)
async def query(
    id: UUID4,
    db_session: DatabaseDependency,
) -> TaxonOut:
    
    taxon: TaxonOut = (
        await db_session.execute(select(TaxonModel).filter_by(id=id))
    ).scalars().first()
    
    if not taxon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Taxon não encontrado pelo ID: {id}"
        )

    return taxon
