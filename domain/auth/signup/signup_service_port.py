from abc import ABC, abstractmethod

from domain.command.model import TutorCreate


class SignupServicePort(ABC):

    @abstractmethod
    def add_tutor(self, tutor: TutorCreate):
        pass

    @abstractmethod
    def tutor_exists(self, username: str) -> bool:
        pass
