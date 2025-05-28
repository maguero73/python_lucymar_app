from pydantic import BaseModel
from datetime import date
from typing import Optional

class GastoCreate(BaseModel):
    cod_gasto: int
    cod_titular: int
    monto: float
    fecha: date
    codigo_moneda: str
    tipo_cambio: float
    fecha_creacion: Optional[date] = None  # opcional si lo carga el backend



