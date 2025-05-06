import flet as ft

from domain.login.login_service_core import LoginServiceCore
from domain.subscription.susbcription_service_core import SubscriptionServiceCore

from ui.app_state import AppState
from ui.app.components.sidebar import Sidebar
from ui.app.auth.auth_view import AuthView
from ui.app.components.snackbar import JSnackbar
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter

from infrastructure.login.login_repository_adapter import LoginRepositoryAdapter


class LoginHandler:
    def __init__(self, login_view: AuthView, page: ft.Page, sidebar: Sidebar):
        self._login_view = login_view
        self._sidebar = sidebar
        self._page = page

    def handle_login(self, event: ft.ControlEvent):
        if self._login_view.not_complet_data:
            snackbar = JSnackbar(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            event.page.open(snackbar)
            return

        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(self._login_view.username_field, self._login_view.password_field)
        
        if not user:
            snackbar = JSnackbar(
                message="Usuario o contraseña incorrectos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            event.page.open(snackbar)
            return

        subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())
        state = AppState(user=user, app=subscription_service.get_user_app(user))

        self._page.theme = state.app.theme
        self._sidebar.keys = {
            self._delete_slash(jview.name): jview.icon 
            for jview in state.app.views.values()
        }
        self._page.views.clear()
        default_view = state.app.views["inicio"].view
        self._page.views.append(default_view)
        if default_view.route:
            self._page.go(default_view.route)
        self._page.update()

    def _delete_slash(self, value: str) -> str:
        return value[1:] if value.startswith("/") else value
