import flet as ft

from domain.login import LoginServiceCore
from domain.subscription import SubscriptionServiceCore
from domain.registration.registration_service_core import RegistrationServiceCore

from ui.app_state import AppState
from ui.app.login.login_view import LoginView
from ui.app.components.sidebar import Sidebar
from ui.app.register_children.payment_dialog import PaymentDialog
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter
from ui.app.register_children.subscription_dialog import SubscriptionDialog
from ui.app.register_children.register_children_view import RegisterChildrenView

from infrastructure.login import LoginRepositoryAdapter
from infrastructure.repository import RegistrationRepositoryAdapter


class AuthController:
    def __init__(self, page: ft.Page):
        self._page = page
        self._sidebar = Sidebar()
        self._login_view = LoginView(
            on_login=self._on_login,
            on_signup=self._on_signup
        )

    def show_login_view(self):
        self._page.views.clear()
        self._page.views.append(self._login_view)
        self._page.go("/login")
        self._page.update()

    def _show_snackbar_message(self, message: str, bgcolor: str, text_color: str) -> None:
        snackbar = ft.SnackBar(
            content=ft.Row(
                [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
        )
        self._page.open(snackbar)

    def _delete_slash(self, value: str) -> str:
        return value[1:] if value.startswith("/") else value

    def _on_login(self, event: ft.ControlEvent):
        if self._login_view.not_complet_data:
            self._show_snackbar_message(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return
        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(self._login_view.username_field, self._login_view.password_field)
        if not user:
            self._show_snackbar_message(
                message="Usuario no encontrado!",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return
        subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())
        state = AppState(user=user, app=subscription_service.get_user_app(user))
        self._page.theme = state.app.theme
        self._sidebar.keys = {
            self._delete_slash(jview.name): jview.icon for jview in state.app.views.values()
        }
        self._page.views.clear()
        default_view = state.app.views["inicio"].view
        self._page.views.append(default_view)
        if default_view.route:
            self._page.go(default_view.route)
        self._page.update()

    def _on_signup(self, event: ft.ControlEvent):
        signup_data = self._login_view.signup.signup_data

        # Validación de campos obligatorios
        if self._login_view.signup.not_completed_data:
            self._show_snackbar_message(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Validación de coincidencia de contraseñas
        if signup_data["password"] != signup_data["confirm_password"]:
            self._show_snackbar_message(
                message="Las contraseñas no coinciden.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Validación de tipo de suscripción (puedes mejorar esto con una consulta a la base de datos)
        subscription_type_name = signup_data["subscription_type"].strip().lower()
        if subscription_type_name not in ["free", "premium"]:
            self._show_snackbar_message(
                message="Tipo de suscripción inválido. Usa 'free' o 'premium'.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Construir el diccionario para el registro
        tutor_data = {
            "username": signup_data["username"],
            "password": signup_data["password"],
            "full_name": signup_data["full_name"],
            "children": [],
            "subscription_type": subscription_type_name
        }

        registration_service = RegistrationServiceCore(RegistrationRepositoryAdapter())
        try:
            # Validar existencia de usuario (esto depende de la implementación del repositorio)
            # Si el repositorio lanza excepción por usuario duplicado, se captura aquí
            registration_service.start_registration(tutor_data)
        except Exception as e:
            self._show_snackbar_message(
                message=f"Error al registrar tutor: {str(e)}",
                bgcolor=ft.Colors.RED_200,
                text_color="#2D2242",
            )
            return

        def on_finish_register_children(children_data):
            def on_subscription_selected(subscription_type):
                registration_service.set_subscription(subscription_type)
                if subscription_type == "premium":
                    def on_payment_success(payment_data):
                        registration_service.process_payment(payment_data)
                        registration_service.finalize_registration()
                        self._show_snackbar_message(
                            message="¡Registro completo y pago exitoso!",
                            bgcolor=ft.Colors.GREEN_200,
                            text_color="#2D2242",
                        )
                        self._page.go("/tutor-app")
                        self._page.update()
                        self._page.close(payment_dialog)
                    payment_dialog = PaymentDialog(on_success=on_payment_success)
                    self._page.open(payment_dialog)
                else:
                    registration_service.finalize_registration()
                    self._show_snackbar_message(
                        message="¡Registro completo! Bienvenido.",
                        bgcolor=ft.Colors.GREEN_200,
                        text_color="#2D2242",
                    )
                    self._page.go("/tutor-app")
                    self._page.update()
            subscription_dialog = SubscriptionDialog(on_select=on_subscription_selected)
            self._page.open(subscription_dialog)
        register_children_view = RegisterChildrenView(
            on_finish=on_finish_register_children,
            registration_service=registration_service
        )
        self._page.views.append(register_children_view)
        self._page.go("/register-child")
        self._page.update()
