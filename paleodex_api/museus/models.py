from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from paleodex_api.contrib.models  import BaseModel
# from paleodex_api.especime.models import EspecimeModel


class MuseuModel(BaseModel):
    __tablename__ = 'museus'
    
    pk_id  : Mapped[int] = mapped_column(Integer,    primary_key=True)
    nome   : Mapped[str] = mapped_column(String(40), nullable=False, unique=True)
    cidade : Mapped[str] = mapped_column(String(20), nullable=False)
    estado : Mapped[str] = mapped_column(String(15), nullable=False)

    especime : Mapped['EspecimeModel'] = relationship(back_populates='museu')
