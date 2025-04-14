from abc import ABC, abstractmethod

from domain.model.model import Child, Nutritionist, Tutor


class AuthRepositoryPort(ABC):
    
    @abstractmethod
    def username_exist(self, value: str) -> bool:
        pass
    
    @abstractmethod
    def password_exist(self, values: str) -> bool:
        pass

    @abstractmethod
    def get_user(self, username: str, password: str) -> Tutor | Child | Nutritionist | None:
        pass
    