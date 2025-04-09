from abc import ABC, abstractmethod

from domain.model.model import User


class AuthServicePort(ABC):
    
    @abstractmethod
    def login(self, username: str, password: str) -> User | None:
        """
        Comprueba si las credenciales de usuario son correctas y devuelve el tipo de usuario correspondiente. Si el usuario no existe, devuelve None.
        """
        pass