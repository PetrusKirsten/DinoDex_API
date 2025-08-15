from typing import Annotated
from pydantic import Field

from dinodex_api.contrib.schemas import BaseSchema


class Taxon(BaseSchema):
    nome: Annotated[
        str, Field(description='Nome do taxon', example='Theropoda', max_length=12)]