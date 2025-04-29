from abc import ABC, abstractmethod
from domain.app import TutorFreeApp, TutorPremiumApp, ChildFreeApp, ChildPremiumApp


class SubscriptionRepositoryPort(ABC):

    @abstractmethod
    def get_tutor_free_app(self) -> TutorFreeApp:
        pass

    @abstractmethod
    def get_tutor_premium_app(self) -> TutorPremiumApp:
        pass

    @abstractmethod
    def get_child_free_app(self) -> ChildFreeApp:
        pass

    @abstractmethod
    def get_child_premium_app(self) -> ChildPremiumApp:
        pass