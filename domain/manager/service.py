from abc import ABC
from typing import TypeVar

from domain.manager.repository import Repository


R = TypeVar('R', bound=Repository)

class Service(ABC):
    """
    Base para todos los servicios que implementan la lógica de negocio. Recibe repositorios como
    dependencias.
    """
    
    def __init__(self, *repositories: Repository) -> None:
        super().__init__()
        self._repositories = repositories
    
    def _get_repository(self, repository_class: type[R]) -> R:
        for repository in self._repositories:
            if isinstance(repository, repository_class):
                return repository
        raise KeyError(f"El repositorio {repository_class.__name__} no está registrado.")
        