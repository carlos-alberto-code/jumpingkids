from abc import ABC, abstractmethod

class RegistrationServicePort(ABC):
    @abstractmethod
    def start_registration(self, tutor_data: dict):
        pass

    @abstractmethod
    def add_child(self, child_data: dict):
        pass

    @abstractmethod
    def set_subscription(self, subscription_type: str):
        pass

    @abstractmethod
    def process_payment(self, payment_data: dict):
        pass

    @abstractmethod
    def finalize_registration(self):
        pass
