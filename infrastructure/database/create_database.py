from infrastructure.database.model import Base
from infrastructure.database.connection import engine


def create_database():
    """Crea todas las tablas en la base de datos."""
    Base.metadata.create_all(engine)
