from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.lm_gastos_test import LMGastoTest
from app.schemas.gasto import GastoIn
from datetime import datetime
import pytz

argentina = pytz.timezone("America/Argentina/Buenos_Aires")
fecha_creacion = datetime.now(argentina)

print(f"📌 Fecha creación generada: {fecha_creacion}")  # DEBUG

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/test")
async def crear_gasto_test(gasto: GastoIn, db: Session = Depends(get_db)):
    try:
        print("Gasto recibido (test):", gasto)
        nuevo_gasto = LMGastoTest(
            cod_gasto=gasto.cod_gasto,
            cod_titular=gasto.cod_titular,
            monto=gasto.monto,
            fecha=gasto.fecha,
            cod_moneda=gasto.cod_moneda,
            tipo_cambio=gasto.tipo_cambio,
            fecha_creacion=gasto.fecha_creacion,
        )
        print("🟡 Antes de add")
        db.add(nuevo_gasto)
        print("🟠 Antes de commit")
        db.commit()
        print("🟢 Commit exitoso")
        return {"mensaje": "Gasto test guardado con éxito"}
    except Exception as e:
        db.rollback()
        print("🔴 Error en test insert:", e)
        raise HTTPException(status_code=500, detail="Error en insert de prueba")