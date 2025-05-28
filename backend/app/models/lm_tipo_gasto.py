from sqlalchemy import Column, Integer, String
from app.core.database import Base

class LMTipoGasto(Base):
    __tablename__ = "LM_TIPO_GASTO"

    codigo = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(20))
