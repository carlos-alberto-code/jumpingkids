from abc import ABC

from interface.repository import Repository


class Service(ABC):
    """
    Base para todos los servicios que implementan la lógica de negocio. Recibe repositorios como
    dependencias.
    """
    
    def __init__(self, *repositories: Repository) -> None:
        super().__init__()
        self._repositories = repositories
        