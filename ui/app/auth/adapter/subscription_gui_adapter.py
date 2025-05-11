

from domain.manager.view_manager import ViewManager
from domain.model.dto import App
from domain.app.auth.subscription.subscription_repository_port import SubscriptionRepositoryPort

from ui.theme.child_free_theme import ChildFreeTheme
from ui.config.child_free_app import view_manager as child_free_view_manager
from ui.config.tutor_free_app import view_manager as tutor_free_view_manager
from ui.config.child_premium_app import view_manager as child_premium_view_manager
from ui.config.tutor_premium_app import view_manager as tutor_premium_view_manager


class SubscriptionGuiAdapter(SubscriptionRepositoryPort):

    def get_child_free_app(self) -> App:
        return App(
            theme=ChildFreeTheme(),
            view_manager=child_free_view_manager
        )
    
    def get_tutor_free_app(self) -> App:
        return App(
            theme=ChildFreeTheme(),
            view_manager=tutor_free_view_manager
        )

    def get_child_premium_app(self) -> App:
        return App(
            theme=ChildFreeTheme(),
            view_manager=child_premium_view_manager
        )
    
    def get_tutor_premium_app(self) -> App:
        return App(
            theme=ChildFreeTheme(),
            view_manager=tutor_premium_view_manager
        )
    