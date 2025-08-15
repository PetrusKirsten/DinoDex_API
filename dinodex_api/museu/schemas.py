from typing import Annotated
from pydantic import Field

from dinodex_api.contrib.schemas import BaseSchema


class Museu(BaseSchema):
    nome: Annotated[
        str, Field(description='Nome do museu', example='Museu do Ipiranga', max_length=40)]
    
    cidade: Annotated[
        str, Field(description='Cidade em que fica o museu', example='Rio de Janeiro', max_length=20)]
    
    pais: Annotated[
        str, Field(description='País em que fica museu', example='Brasil', max_length=15)]