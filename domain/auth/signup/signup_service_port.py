from abc import ABC, abstractmethod

from domain.model import Child, Tutor


class SignupServicePort(ABC):

    @abstractmethod
    def add_child(self, child: Child):
        pass

    @abstractmethod
    def add_tutor(self, tutor: Tutor):
        pass

    @abstractmethod
    def tutor_exists(self, username: str) -> bool:
        pass
