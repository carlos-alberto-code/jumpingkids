from abc import ABC, abstractmethod

from domain.app import App

class SubscriptionRepositoryPort(ABC):

    @abstractmethod
    def get_tutor_free_app(self) -> App:
        pass

    @abstractmethod
    def get_tutor_premium_app(self) -> App:
        pass

    @abstractmethod
    def get_child_free_app(self) -> App:
        pass

    @abstractmethod
    def get_child_premium_app(self) -> App:
        pass
    