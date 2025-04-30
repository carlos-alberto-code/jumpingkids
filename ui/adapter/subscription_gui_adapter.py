from domain.app import JumpingkidsTheme
from domain.subscription import SubscriptionRepositoryPort
from domain.app import App, ChildFreeApp, ChildPremiumApp, TutorFreeApp, TutorPremiumApp

from ui.theme.child_free_theme import ChildFreeTheme


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
        app = self._apps["child_free"](theme)
        return app
    
    def get_tutor_free_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["tutor_free"](theme)
        return app

    def get_child_premium_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["child_premium"](theme)
        return app
    
    def get_tutor_premium_app(self) -> App:
        theme = self._themes["child_free"]()
        app = self._apps["tutor_premium"](theme)
        return app
    