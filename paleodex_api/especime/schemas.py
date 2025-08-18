from typing   import Annotated, Optional
from pydantic import Field, PositiveFloat

from paleodex_api.contrib.schemas import BaseSchema, OutMixin
from paleodex_api.museus.schemas  import MuseuEspecime
from paleodex_api.taxons.schemas  import TaxonIn


class Especime(BaseSchema):
    apelido: Annotated[
        str, 
        Field(description='Apelido do fóssil', 
              example='Unaysaurus tolentinoi', 
              max_length=50)
    ]
    
    codigo: Annotated[
        str, 
        Field(description='Código do espécime', 
              example='1001', 
              max_length=8)
    ]
    
    idade: Annotated[
        PositiveFloat, 
        Field(description='Idade do fóssil estimada em milhões', 
              example=200)
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

    taxon: Annotated[
        TaxonIn, 
        Field(description='Taxon do espécime')
    ]
    
    museu: Annotated[
        MuseuEspecime, 
        Field(description='Museu do espécime')
    ]
    


class EspecimeIn(Especime):
    pass


class EspecimeOut(Especime, OutMixin):
    pass


class EspecimeUpdate(BaseSchema):
    apelido: Annotated[
        Optional[str], 
        Field(None,
              description = 'Apelido do fóssil', 
              example     = 'Blue', 
              max_length  = 50)
    ]
    
    codigo: Annotated[
        Optional[str], 
        Field(None,
              description = 'Código do espécime', 
              example     = '101', 
              max_length  = 8)
    ]
