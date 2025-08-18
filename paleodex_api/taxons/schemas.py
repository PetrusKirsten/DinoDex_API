from typing import Annotated
from pydantic import UUID4, Field

from paleodex_api.contrib.schemas import BaseSchema


class TaxonIn(BaseSchema):
    nome: Annotated[
        str,
        Field(description='Nome do taxon',
              example='Theropoda',
              max_length=12)
        ]
    

class TaxonOut(TaxonIn):
    id: Annotated[UUID4, Field(description="Identificador do taxon")]
