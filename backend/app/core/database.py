from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Reemplazá estos datos con los de tu entorno real
ORACLE_USER = "SYSTEM"
ORACLE_PASSWORD = "maguero"
ORACLE_HOST = "localhost"
ORACLE_PORT = "61521"
ORACLE_SID = "XE"  # o el SERVICE_NAME, como "orclpdb1"

# 🔧 URL para conexión a Oracle
DATABASE_URL = (
    f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_HOST}:{ORACLE_PORT}/?service_name={ORACLE_SID}"
)

# Crear el engine
engine = create_engine(DATABASE_URL, echo=True)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()