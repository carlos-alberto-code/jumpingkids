from abc import ABC, abstractmethod

from domain.model.model import Tutor, Child


class LoginServicePort(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> Tutor | Child | None:
        pass
    