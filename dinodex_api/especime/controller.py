from fastapi  import APIRouter, Body, HTTPException, status
from uuid     import uuid4
from datetime import datetime

from sqlalchemy.future import select

from dinodex_api.contrib.dependencies import DatabaseDependency
from dinodex_api.especime.schemas     import EspecimeIn, EspecimeOut
from dinodex_api.especime.models      import EspecimeModel
from dinodex_api.museus.models        import MuseuModel
from dinodex_api.taxons.models        import TaxonModel

router = APIRouter()

@router.post(
        "/", 
        summary="Catalogar um novo espécime",
        status_code=status.HTTP_201_CREATED,
        response_model=EspecimeOut,
)
async def post(
    db_session: DatabaseDependency,
    especime_in: EspecimeIn = Body(...)
) -> EspecimeOut:

    taxon_nome = especime_in.taxon.nome
    museu_nome = especime_in.museu.nome

    taxon = (
        await db_session.execute(
            select(TaxonModel).filter_by(nome=taxon_nome))
    ).scalars().first()
    
    if not taxon:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail      = f"O taxon '{taxon_nome}' não foi encontrado."
        )
    
    museu = (
        await db_session.execute(
            select(MuseuModel).filter_by(nome=museu_nome))
    ).scalars().first()

    if not museu:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST, 
            detail      = f"O museu '{museu_nome}' não foi encontrado."
        )
    # breakpoint()
    try:
        especime_out   = EspecimeOut(id           = uuid4(), 
                                    catalogado_em = datetime.utcnow(), 
                                    **especime_in.model_dump(),)
        
        especime_model = EspecimeModel(**especime_out.model_dump(exclude={'taxon', 'museu'}))
        especime_model.taxon_id = taxon.pk_id
        especime_model.museu_id = museu.pk_id

        db_session.add(especime_model)
        await db_session.commit()

    except Exception as exc:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail      = f"Ocorreu um erro ao inserir os dados no banco: {exc}."
        )
        

    return especime_out


@router.get(
        "/", 
        summary        = "Consultar todos os espécimes",
        status_code    = status.HTTP_200_OK,
        response_model = list[EspecimeOut],
)
async def query(
    db_session: DatabaseDependency,
) -> list[EspecimeOut]:
    
    especimes: list[EspecimeOut] = (
        await db_session.execute(select(EspecimeModel))
        ).scalars().all()
    
    return [EspecimeOut.model_validate(especime) for especime in especimes]
    