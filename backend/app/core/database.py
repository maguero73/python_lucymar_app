import mariadb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text

# URL de conexión (ajustala a tu configuración real)
DATABASE_URL = "mariadb+mariadbconnector://lucymar_user:Admin@192.168.0.9:3306/lucymar_db"

# Crear el motor (engine)
engine = create_engine(
    DATABASE_URL,
    echo=True  # Podés poner False si no querés ver las consultas en consola
)

# Crear una sesión local para usar en cada request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir tus modelos ORM
Base = declarative_base()



#INTENTAR UNA CONSULTA BASICA A LA BASE
"""

try:
    with engine.connect() as connection:
        result=connection.execute(text("SELECT 1"))
        print("conexion exitosa:", result.scalar())
except Exception as e:
    print("Error al conectar:", e)        

"""