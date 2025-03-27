from abc import ABC, abstractmethod

from hexagon.domain.model import Child, Tutor


class ChildSessionServicePort(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> Child | None:
        """
        Comprueba si las credenciales de usuario son correctas y devuelve el usuario correspondiente. Si el usuario no existe, devuelve None.
        """
        pass