from domain.app import ChildFreeApp, ChildPremiumApp, TutorFreeApp, TutorPremiumApp
from domain.subscription import SubscriptionRepositoryPort


class SubscriptionGuiAdapter(SubscriptionRepositoryPort):

    def get_child_free_app(self) -> ChildFreeApp:
        ...
    
    def get_tutor_free_app(self) -> TutorFreeApp:
        ...

    def get_child_premium_app(self) -> ChildPremiumApp:
        ...
    
    def get_tutor_premium_app(self) -> TutorPremiumApp:
        ...