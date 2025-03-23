from sqlalchemy import MetaData
from infrastructure.persistence.database.connection import engine


metadata = MetaData()

def create_database():
    """Crea todas las tablas en la base de datos."""
    metadata.create_all(engine)
