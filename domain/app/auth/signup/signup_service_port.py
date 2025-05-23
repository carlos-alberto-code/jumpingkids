from abc import ABC, abstractmethod

from domain.model.command import TutorCreate
from domain.model.model import SubscriptionType


class SignupServicePort(ABC):

    @abstractmethod
    def add_tutor(self, tutor: TutorCreate):
        pass

    @abstractmethod
    def tutor_exists(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_subscription_types(self) -> list[SubscriptionType]:
        pass
