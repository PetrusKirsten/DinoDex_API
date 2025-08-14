from typing import Annotated
from pydantic import Field

from dinodex_api.contrib.schemas import BaseSchema


class Museu(BaseSchema):
    nome: Annotated[
        str, Field(description='Nome do museu', examples='Museu de História Natural', max_length=50)]
    
    endereco: Annotated[
        str, Field(description='Nome do museu', examples='Museu de História Natural', max_length=50)]
    
    nome: Annotated[
        str, Field(description='Nome do museu', examples='Museu de História Natural', max_length=50)]