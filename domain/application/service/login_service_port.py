from abc import ABC, abstractmethod

from domain.model.model import Tutor, Child
from domain.application.repository import LoginRepositoryPort


class LoginServicePort(ABC):

    def __init__(self, login_repository: LoginRepositoryPort) -> None:
        super().__init__()
        self._login_repository = login_repository

    
    @abstractmethod
    def login(self, username: str, password: str) -> Tutor | Child | None:
        """
        Devuelve el tipo de usuario correspondiente a las credenciales ingresadas. Si el usuario no existe, devuelve ``None``.
        """
        pass