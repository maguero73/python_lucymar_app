from sqlalchemy import Column, Integer, String
from app.core.database import Base

class LMTitular(Base):
    __tablename__ = "LM_TITULAR"

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20))
