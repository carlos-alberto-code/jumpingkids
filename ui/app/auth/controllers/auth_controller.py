import flet as ft

from domain.auth.login.login_service_core import LoginServiceCore
from domain.auth.signup.signup_service_core import SignupServiceCore
from domain.auth.subscription.susbcription_service_core import SubscriptionServiceCore

from ui.app.auth.auth_view import AuthView
from ui.app.components.sidebar import Sidebar
from ui.app.auth.controllers.login_handler import LoginHandler
from ui.app.auth.controllers.signup_handler import SignupHandler
from ui.app.auth.adapter.subscription_gui_adapter import SubscriptionGuiAdapter

from infrastructure.auth.login.login_repository_adapter import LoginRepositoryAdapter
from infrastructure.auth.signup.signup_service_adapter import SignupRepositoryAdapter


class AuthController:
    def __init__(self, page: ft.Page):
        self._page = page
        self._sidebar = Sidebar()
        
        login_service = LoginServiceCore(LoginRepositoryAdapter())
        signup_service = SignupServiceCore(SignupRepositoryAdapter())
        subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())

        self._auth_view = AuthView(
            subscription_types=signup_service.get_subscription_types(),
            on_login=self._login_handler.handle_login,
            on_signup=self._signup_handler.handle_signup
        )


        self._login_handler = LoginHandler(self._auth_view, login_service, subscription_service)
        self._signup_handler = SignupHandler(self._auth_view, signup_service)

    def show_auth_view(self):
        self._page.views.clear()
        self._page.views.append(self._auth_view)
        self._page.go("/auth")
        self._page.update()
