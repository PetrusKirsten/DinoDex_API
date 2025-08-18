from pydantic import UUID4, Field
from typing   import Annotated

from paleodex_api.contrib.schemas import BaseSchema


class MuseuIn(BaseSchema):
    nome: Annotated[
        str, 
        Field(description = 'Nome do museu', 
              example     = 'Museu Nacional', 
              max_length  = 40)
        ]
    
    cidade: Annotated[
        str, 
        Field(description = 'Cidade do museu', 
              example     = 'Rio de Janeiro', 
              max_length  = 20)
        ]
    
    estado: Annotated[
        str, 
        Field(description = 'Estado (UF) do museu', 
              example     = 'RJ', 
              max_length  = 15)
        ]


class MuseuEspecime(BaseSchema):
    nome: Annotated[
        str, 
        Field(description = 'Nome do museu', 
              example     = 'Museu do Ipiranga', 
              max_length  = 40)
        ]


class MuseuOut(MuseuIn):
    id: Annotated[
        UUID4, 
        Field(description="Identificador do museu")]
