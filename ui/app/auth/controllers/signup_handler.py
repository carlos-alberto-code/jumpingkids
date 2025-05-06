import flet as ft

from domain.model import SubscriptionType, Tutor
from domain.auth.signup.signup_service_port import SignupServicePort

from ui.app.auth.auth_view import AuthView
from ui.app.components.snackbar import JSnackbar


class SignupHandler:
    def __init__(self, auth_view: AuthView, signup_service: SignupServicePort):
        self._auth_view = auth_view
        self._signup_service = signup_service

    def handle_signup(self, event: ft.ControlEvent):
        if not self._is_form_complete(event):
            return
        tutor = self._build_tutor_from_form()
        if self._signup_service.tutor_exists(tutor.username):
            self._show_snackbar(event, "El usuario ya existe!", ft.Colors.RED_400)
            return
        try:
            self._signup_service.add_tutor(tutor)
            self._show_snackbar(event, "Usuario creado correctamente!", ft.Colors.GREEN_400)
        except Exception:
            self._show_snackbar(event, "Error al crear el usuario!", ft.Colors.RED_400)
            return
        self._auth_view.panel.show_login()

    def _is_form_complete(self, event: ft.ControlEvent) -> bool:
        if not self._auth_view.panel.signup_form.completed_data:
            self._show_snackbar(event, "Por favor, rellena todos los campos!", ft.Colors.RED_400)
            return False
        return True

    def _build_tutor_from_form(self) -> Tutor:
        form = self._auth_view.panel.signup_form
        return Tutor(
            id=None,
            username=form.username,
            password=form.password,
            full_name=form.full_name,
            children=None,
            subscription_type=SubscriptionType(
                id=None,
                name=form.subscription_type,
            ),
        )

    def _show_snackbar(self, event: ft.ControlEvent, message: str, bgcolor: str):
        event.page.open(
            JSnackbar(
                message=message,
                bgcolor=bgcolor,
                text_color=ft.Colors.WHITE,
            )
        )
