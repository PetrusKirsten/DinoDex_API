from datetime import datetime
from typing   import Annotated
from pydantic import Field, PositiveFloat

from dinodex_api.contrib.schemas import BaseSchema, OutMixin


class Especime(BaseSchema):
    apelido: Annotated[
        str, 
        Field(description='Apelido do fóssil', 
              example='Blue', 
              max_length=50)
        ]
    
    codigo: Annotated[
        str, 
        Field(description='Código do espécime', 
              example='101', 
              max_length=8)
        ]
    
    idade: Annotated[
        PositiveFloat, 
        Field(description='Idade do fósisl estimada em milhões', 
              example=60)
        ]

    peso: Annotated[
        PositiveFloat, 
        Field(description='Massa estimada em kilogramas', 
              example=525.0)
            ]

    altura: Annotated[
        PositiveFloat, 
        Field(description='Altura estimada em metros',
              example=1.5)
            ]

    conservacao: Annotated[
        str, 
        Field(description='Estado de conservação do espécime ("excelente", "bom", "parcial", "fragmentado")', 
              example='bom')
        ]

    catalogado_em: Annotated[
        datetime, 
        Field(description='Data em que o espécime foi catalogado no museu', 
              )
        ]  # example='bom')]

    # museu_id: Annotated[
    #     str, 
    #     Field(description='Estado de conservação do espécime', example=1.5, max_length=8)]
    
    # taxon_id: Annotated[
    #     str, 
    #     Field(description='Estado de conservação do espécime', example=1.5, max_length=8)]


class EspecimeIn(Especime):
    pass


class EspecimeOut(Especime, OutMixin):
    pass
