from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dinodex_api.contrib.models import BaseModel


class TaxonModel(BaseModel):
    __tablename__ = 'taxons'
    
    pk_id : Mapped[int] = mapped_column(Integer,    primary_key=True)
    nome  : Mapped[str] = mapped_column(String(50), nullable=False)

    especime : Mapped['EspecimeModel'] = relationship(back_populates='taxon')
