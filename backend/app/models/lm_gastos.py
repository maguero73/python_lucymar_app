from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class LMGasto(Base):
    __tablename__ = "LM_GASTOS"

    id = Column(Integer, primary_key=True, index=True)
    cod_gasto = Column(Integer, nullable=False)
    cod_titular = Column(Integer, nullable=False)
    monto = Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)
    codigo_moneda = Column(String(3), nullable=True)
    tipo_cambio = Column(Float, nullable=True)
    fecha_creacion = Column(Date, nullable=True)
