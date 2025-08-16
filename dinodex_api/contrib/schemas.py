from typing import Annotated
from pydantic   import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="Identificador")]
    catalogado_em: Annotated[datetime, Field("Data em que o espécime foi catalogado no museu")]
