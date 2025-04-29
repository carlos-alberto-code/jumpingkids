from domain.app import App
from domain.model import Child, Tutor
from domain.subscription.subscription_service_port import SubscriptionServicePort
from domain.subscription.subscription_repository_port import SubscriptionRepositoryPort


class SubscriptionServiceCore(SubscriptionServicePort):

    def __init__(self, subscription_repository: SubscriptionRepositoryPort) -> None:
        super().__init__()
        self._subscription_repository = subscription_repository
    
    def get_user_app(self, user: Tutor | Child) -> App:
        if isinstance(user, Tutor):
            return self._subscription_repository.get_tutor_app()
        elif isinstance(user, Child):
            return self._subscription_repository.get_child_app()
