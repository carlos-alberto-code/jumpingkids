from abc import ABC, abstractmethod

class RegistrationRepositoryPort(ABC):
    @abstractmethod
    def save_tutor(self, tutor_data: dict):
        pass

    @abstractmethod
    def save_children(self, tutor_id: int, children_data: list):
        pass

    @abstractmethod
    def save_subscription(self, tutor_id: int, subscription_type: str):
        pass
