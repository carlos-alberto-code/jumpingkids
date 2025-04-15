from abc import ABC, abstractmethod

from domain.model.model import Child, Tutor


class LoginRepositoryPort(ABC):

    @abstractmethod
    def get_user_by_credentials(self, username: str, password: str) -> Tutor | Child | None:
        pass
    