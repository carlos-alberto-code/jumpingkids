from abc import ABC, abstractmethod
from domain.app import TutorFreeApp, TutorPremiumApp, ChildFreeApp, ChildPremiumApp


class SubscriptionRepositoryPort(ABC):

    @abstractmethod
    def get_tutor_app(self) -> TutorFreeApp | TutorPremiumApp:
        pass

    @abstractmethod
    def get_child_app(self) -> ChildFreeApp | ChildPremiumApp:
        pass