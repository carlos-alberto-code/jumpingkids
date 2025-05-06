from abc import ABC, abstractmethod

from domain.model import Child, Tutor

class SignupRepositoryPort(ABC):
    
    @abstractmethod
    def save_tutor(self, tutor: Tutor):
        pass

    @abstractmethod
    def save_children(self, children: Child):
        pass
