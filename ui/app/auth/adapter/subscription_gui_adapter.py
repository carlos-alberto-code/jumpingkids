from domain.app import App

from domain.auth.subscription.subscription_repository_port import SubscriptionRepositoryPort
from ui.theme.child_free_theme import ChildFreeTheme

from ui.config.child_free_app import view_manager as child_free_view_manager
from ui.config.tutor_free_app import view_manager as tutor_free_view_manager
from ui.config.child_premium_app import view_manager as child_premium_view_manager
from ui.config.tutor_premium_app import view_manager as tutor_premium_view_manager


class SubscriptionGuiAdapter(SubscriptionRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
        self._apps: dict[str, type[App]] = {
            "child_free": ChildFreeApp,
            "tutor_free": TutorFreeApp,
            "child_premium": ChildPremiumApp,
            "tutor_premium": TutorPremiumApp
        }
        self._themes: dict[str, type[JumpingkidsTheme]] = {
            "child_free": ChildFreeTheme,
        }

    def get_child_free_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["child_free"](theme, child_free_view_manager)
        return app
    
    def get_tutor_free_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["tutor_free"](theme, tutor_free_view_manager)
        return app

    def get_child_premium_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["child_premium"](theme, child_premium_view_manager)
        return app
    
    def get_tutor_premium_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["tutor_premium"](theme, tutor_premium_view_manager)
        return app
    