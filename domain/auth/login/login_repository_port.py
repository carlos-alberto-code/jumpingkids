from abc import ABC, abstractmethod

from domain.model import Tutor, Child


class LoginRepositoryPort(ABC):

    @abstractmethod
    def get_by_username(self, username: str) -> Tutor | Child | None:
        pass
