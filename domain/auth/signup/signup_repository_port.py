from abc import ABC, abstractmethod

from domain.command.model import TutorCreate


class SignupRepositoryPort(ABC):
    
    @abstractmethod
    def save_tutor(self, tutor: TutorCreate):
        pass
    
    @abstractmethod
    def tutor_exists(self, username: str) -> bool:
        pass
