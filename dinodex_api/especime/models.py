from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dinodex_api.contrib.models import BaseModel


class EspecimeModel(BaseModel):
    __tablename__ = 'espécimes'
    
    pk_id         : Mapped[int]      = mapped_column(Integer,    primary_key=True)
    apelido       : Mapped[str]      = mapped_column(String(50), nullable=False)
    codigo        : Mapped[str]      = mapped_column(String(11), nullable=False)
    idade         : Mapped[int]      = mapped_column(Integer,    nullable=False)
    peso          : Mapped[float]    = mapped_column(Float,      nullable=False)
    altura        : Mapped[float]    = mapped_column(Float,      nullable=False)
    conservacao   : Mapped[str]      = mapped_column(String(11), nullable=False)
    catalogado_em : Mapped[datetime] = mapped_column(DateTime,   nullable=False)

    taxon    : Mapped['TaxonModel'] = relationship(back_populates='espécime')
    taxon_id : Mapped[int] = mapped_column(ForeignKey('taxons.pk_id'))
