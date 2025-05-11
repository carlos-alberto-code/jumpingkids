from abc import ABC, abstractmethod

from domain.model.dto import App
from domain.model.model import Tutor, Child


class SubscriptionServicePort(ABC):

    @abstractmethod
    def get_user_app(self, user: Tutor | Child) -> App: pass
    