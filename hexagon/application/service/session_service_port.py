from abc import ABC, abstractmethod

from hexagon.domain.model import Child, Tutor


class SessionServicePort(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> Tutor | Child | None:
        """
        Comprueba si las credenciales de usuario son correctas y devuelve el usuario correspondiente. Si el usuario no existe, devuelve None.
        """
        pass