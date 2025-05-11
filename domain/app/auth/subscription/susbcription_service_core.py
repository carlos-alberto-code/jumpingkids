from domain.model.dto import App
from domain.model.model import Child, Tutor
from domain.app.auth.subscription.subscription_service_port import SubscriptionServicePort
from domain.app.auth.subscription.subscription_repository_port import SubscriptionRepositoryPort


class SubscriptionServiceCore(SubscriptionServicePort):

    def __init__(self, subscription_repository: SubscriptionRepositoryPort) -> None:
        super().__init__()
        self._subscription_repository = subscription_repository
    
    def get_user_app(self, user: Tutor | Child) -> App:
        if isinstance(user, Tutor):
            if user.subscription_type.name == "free":
                return self._subscription_repository.get_tutor_free_app()
            if user.subscription_type.name == "premium":
                return self._subscription_repository.get_tutor_premium_app()
        if isinstance(user, Child):
            if user.tutor.subscription_type.name == "free":
                return self._subscription_repository.get_child_free_app()
            if user.tutor.subscription_type.name == "premium":
                return self._subscription_repository.get_child_premium_app()

        raise ValueError(f"No fue posible obtener la aplicación para el usuario: {user}")
