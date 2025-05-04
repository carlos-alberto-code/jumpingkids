"""
AuthController: Encapsula la lógica de login y registro de usuarios (tutores).
Responsabilidad: Manejar el flujo de autenticación y registro, delegando a servicios y adaptadores.
"""
import flet as ft
from domain.model import Tutor
from domain.login import LoginServiceCore
from domain.subscription import SubscriptionServiceCore
from infrastructure.login import LoginRepositoryAdapter
from ui.app_state import AppState
from ui.app.login.login_view import LoginView
from ui.app.components.sidebar import Sidebar
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter
from domain.registration.registration_service_core import RegistrationServiceCore
from infrastructure.repository import RegistrationRepositoryAdapter
from ui.app.register_children.register_children_view import RegisterChildrenView
from ui.app.register_children.subscription_dialog import SubscriptionDialog
from ui.app.register_children.payment_dialog import PaymentDialog
from domain.model import SubscriptionType

class AuthController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.sidebar = Sidebar()
        self.login_view = LoginView(
            on_login=self.on_login,
            on_signup=self.on_signup
        )

    def show_login_view(self):
        self.page.views.clear()
        self.page.views.append(self.login_view)
        self.page.go("/login")
        self.page.update()

    def show_snackbar_message(self, message: str, bgcolor: str, text_color: str) -> None:
        snackbar = ft.SnackBar(
            content=ft.Row(
                [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
        )
        self.page.open(snackbar)

    def delete_slash(self, value: str) -> str:
        return value[1:] if value.startswith("/") else value

    def on_login(self, event: ft.ControlEvent):
        if self.login_view.not_complet_data:
            self.show_snackbar_message(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return
        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(self.login_view.username_field, self.login_view.password_field)
        if not user:
            self.show_snackbar_message(
                message="Usuario no encontrado!",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return
        subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())
        state = AppState(user=user, app=subscription_service.get_user_app(user))
        self.page.theme = state.app.theme
        self.sidebar.keys = {
            self.delete_slash(jview.name): jview.icon for jview in state.app.views.values()
        }
        self.page.views.clear()
        default_view = state.app.views["inicio"].view
        self.page.views.append(default_view)
        if default_view.route:
            self.page.go(default_view.route)
        self.page.update()

    def on_signup(self, event: ft.ControlEvent):
        signup_data = self.login_view.signup.signup_data

        # Validación de campos obligatorios
        if self.login_view.signup.not_completed_data:
            self.show_snackbar_message(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Validación de coincidencia de contraseñas
        if signup_data["password"] != signup_data["confirm_password"]:
            self.show_snackbar_message(
                message="Las contraseñas no coinciden.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Validación de tipo de suscripción (puedes mejorar esto con una consulta a la base de datos)
        subscription_type_name = signup_data["subscription_type"].strip().lower()
        if subscription_type_name not in ["free", "premium"]:
            self.show_snackbar_message(
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
            self.show_snackbar_message(
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
                        self.show_snackbar_message(
                            message="¡Registro completo y pago exitoso!",
                            bgcolor=ft.Colors.GREEN_200,
                            text_color="#2D2242",
                        )
                        self.page.go("/tutor-app")
                        self.page.update()
                    self.page.dialog = PaymentDialog(on_success=on_payment_success)
                    self.page.dialog.open = True
                    self.page.update()
                else:
                    registration_service.finalize_registration()
                    self.show_snackbar_message(
                        message="¡Registro completo! Bienvenido.",
                        bgcolor=ft.Colors.GREEN_200,
                        text_color="#2D2242",
                    )
                    self.page.go("/tutor-app")
                    self.page.update()
            self.page.dialog = SubscriptionDialog(on_select=on_subscription_selected)
            self.page.dialog.open = True
            self.page.update()
        register_children_view = RegisterChildrenView(
            on_finish=on_finish_register_children,
            registration_service=registration_service
        )
        self.page.views.append(register_children_view)
        self.page.go("/register-child")
        self.page.update()
