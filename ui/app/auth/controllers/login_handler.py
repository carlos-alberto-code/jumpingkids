import flet as ft

from domain.auth.login.login_service_port import LoginServicePort
from domain.subscription.subscription_service_port import SubscriptionServicePort

from ui.app_state import AppState
from ui.app.auth.auth_view import AuthView
from ui.app.components.snackbar import JSnackbar


class LoginHandler:
    def __init__(self, auth_view: AuthView, login_service: LoginServicePort, subscription_service: SubscriptionServicePort):
        self._auth_view = auth_view
        self._login_service = login_service
        self._subscription_service = subscription_service

    def handle_login(self, event: ft.ControlEvent):
        if not self._auth_view.panel.login_form.completed_data:
            snackbar = JSnackbar(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            event.page.open(snackbar)
            return
        username = self._auth_view.panel.login_form.username_field.value
        password = self._auth_view.panel.login_form.password_field.value
        if username and password:
            user = self._login_service.login(username, password)
        
        if not user:
            snackbar = JSnackbar(
                message="Usuario no encontrado!.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            event.page.open(snackbar)
            return

        # Manejo de la suscripción: Lógica para devolver las vistas para el tipo de usuario y su tipo de suscripción
        
        user_app = self._subscription_service.get_user_app(user)
        state = AppState(user=user, app=user_app)

    def _delete_slash(self, value: str) -> str:
        return value[1:] if value.startswith("/") else value
