from infrastructure.persistence.model import Base
from infrastructure.persistence.database.connection import engine




def create_database():
    """Crea todas las tablas en la base de datos."""
    Base.metadata.create_all(engine)
