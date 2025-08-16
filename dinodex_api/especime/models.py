from datetime   import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float

from sqlalchemy.orm import Mapped, mapped_column, relationship

from dinodex_api.contrib.models import BaseModel
# from dinodex_api.museu.models   import MuseuModel
# from dinodex_api.taxons.models  import TaxonModel


class EspecimeModel(BaseModel):
    __tablename__ = 'especimes'
    
    pk_id         : Mapped[int]      = mapped_column(Integer,    primary_key=True)
    apelido       : Mapped[str]      = mapped_column(String(50), nullable=False)
    codigo        : Mapped[str]      = mapped_column(String(11), nullable=False, unique=True)
    idade         : Mapped[int]      = mapped_column(Integer,    nullable=False)
    peso          : Mapped[float]    = mapped_column(Float,      nullable=False)
    altura        : Mapped[float]    = mapped_column(Float,      nullable=False)
    conservacao   : Mapped[str]      = mapped_column(String(11), nullable=False)
    catalogado_em : Mapped[datetime] = mapped_column(DateTime,   nullable=False)

    taxon    : Mapped['TaxonModel'] = relationship(back_populates='especime', lazy='selectin')
    taxon_id : Mapped[int] = mapped_column(ForeignKey('taxons.pk_id'))

    museu    : Mapped['MuseuModel'] = relationship(back_populates='especime', lazy='selectin')
    museu_id : Mapped[int] = mapped_column(ForeignKey('museus.pk_id'))
