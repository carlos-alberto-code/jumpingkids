import flet as ft

from domain.auth.login.login_service_core import LoginServiceCore
from domain.auth.signup.signup_repository_port import SignupRepositoryPort
from domain.auth.signup.signup_service_core import SignupServiceCore
from infrastructure.auth.signup.signup_service_adapter import SignupRepositoryAdapter
from infrastructure.login.login_repository_adapter import LoginRepositoryAdapter
from ui.app.components.sidebar import Sidebar
from ui.app.auth.auth_view import AuthView
from ui.app.auth.controllers.login_handler import LoginHandler
from ui.app.auth.controllers.signup_handler import SignupHandler


class AuthController:
    def __init__(self, page: ft.Page):
        self._page = page
        self._sidebar = Sidebar()
        
        self._login_view = AuthView(
            on_login=self._login_handler.handle_login,
            on_signup=self._signup_handler.handle_signup
        )

        login_service = LoginServiceCore(LoginRepositoryAdapter())
        signup_service = SignupServiceCore(SignupRepositoryAdapter())

        self._login_handler = LoginHandler(self._login_view, login_service)
        self._signup_handler = SignupHandler(self._login_view, signup_service)

    def show_auth_view(self):
        self._page.views.clear()
        self._page.views.append(self._login_view)
        self._page.go("/auth")
        self._page.update()
