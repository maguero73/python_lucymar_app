from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import SessionLocal
from app.models.lm_gastos import LMGasto
from app.schemas.gasto import GastoCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def crear_gasto(gasto: GastoCreate, db: Session = Depends(get_db)):
    print("📥 Gasto recibido:", gasto)
    nuevo_gasto = LMGasto(
        cod_gasto=gasto.cod_gasto,
        cod_titular=gasto.cod_titular,
        monto=gasto.monto,
        fecha=gasto.fecha,
        codigo_moneda=gasto.codigo_moneda,
        tipo_cambio=gasto.tipo_cambio,
        fecha_creacion=datetime.now()
    )
    db.add(nuevo_gasto)
    db.commit()
    return {"mensaje": "Gasto guardado con éxito"}
