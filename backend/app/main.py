from app.api.endpoints import titulares
from app.api.endpoints import tipo_gasto
from app.api.endpoints import gastos
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI


app = FastAPI(title="Backend-FastAPI")

# --------------Routers------------------
app.include_router(titulares.router, prefix="/api/titulares", tags=["Titulares"])
app.include_router(tipo_gasto.router, prefix="/api/tipos-gasto", tags=["Tipo Gasto"])
app.include_router(gastos.router, prefix="/api/gastos", tags=["Gastos"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # O "*" si estás probando
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

