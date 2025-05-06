import flet as ft

from ui.app.components.sidebar import Sidebar
from ui.app.auth.login.login_view import LoginView
from ui.app.auth.controllers.login_handler import LoginHandler
from ui.app.auth.controllers.signup_handler import SignupHandler


class AuthController:
    def __init__(self, page: ft.Page):
        self._page = page
        self._sidebar = Sidebar()
        self._login_view = LoginView(
            on_login=self._login_handler.handle_login,
            on_signup=self._signup_handler.handle_signup
        )
        self._login_handler = LoginHandler(self._login_view, self._page, self._sidebar)
        self._signup_handler = SignupHandler(self._login_view, self._page)

    def show_login_view(self):
        self._page.views.clear()
        self._page.views.append(self._login_view)
        self._page.go("/login")
        self._page.update()
