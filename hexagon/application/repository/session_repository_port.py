from abc import ABC, abstractmethod

from hexagon.domain.model import Child, Tutor


class SessionRepositoryPort(ABC):

    @abstractmethod
    def get_user(self, username: str) -> Child | None:
        """
        Comprueba si las credenciales de usuario son correctas y devuelve el usuario correspondiente.
        """
        pass