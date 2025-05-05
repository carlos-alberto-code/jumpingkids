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


class UIFeedbackService:
    def __init__(self, page: ft.Page):
        self._page = page

    def show_snackbar(self, message: str, bgcolor: str, text_color: str):
        snackbar = ft.SnackBar(
            content=ft.Row(
                [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
        )
        self._page.open(snackbar)

class LoginHandler:
    def __init__(self, login_view, page: ft.Page, sidebar, feedback_service: UIFeedbackService):
        self._login_view = login_view
        self._page = page
        self._sidebar = sidebar
        self._feedback = feedback_service

    def handle_login(self, event: ft.ControlEvent):
        if self._login_view.not_complet_data:
            self._feedback.show_snackbar(
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return
        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(self._login_view.username_field, self._login_view.password_field)
        if not user:
            self._feedback.show_snackbar(
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

    def _delete_slash(self, value: str) -> str:
        return value[1:] if value.startswith("/") else value

class SignupHandler:
    def __init__(self, login_view, page: ft.Page, feedback_service: UIFeedbackService):
        self._login_view = login_view
        self._page = page
        self._feedback = feedback_service

    def handle_signup(self, event: ft.ControlEvent):
        signup_data = self._login_view.signup.signup_data
        subscription_type_name = signup_data["subscription_type"].strip().lower()
        tutor_data = {
            "username": signup_data["username"],
            "password": signup_data["password"],
            "full_name": signup_data["full_name"],
            "children": [],
            "subscription_type": subscription_type_name
        }
        registration_service = RegistrationServiceCore(RegistrationRepositoryAdapter())
        try:
            registration_service.start_registration(tutor_data)
        except Exception as e:
            self._feedback.show_snackbar(
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
                        self._feedback.show_snackbar(
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
                    self._feedback.show_snackbar(
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

class AuthController:
    def __init__(self, page: ft.Page):
        self._page = page
        self._sidebar = Sidebar()
        self._login_view = LoginView(
            on_login=self._on_login,
            on_signup=self._on_signup
        )
        self._feedback = UIFeedbackService(self._page)
        self._login_handler = LoginHandler(self._login_view, self._page, self._sidebar, self._feedback)
        self._signup_handler = SignupHandler(self._login_view, self._page, self._feedback)

    def show_login_view(self):
        self._page.views.clear()
        self._page.views.append(self._login_view)
        self._page.go("/login")
        self._page.update()

    def _on_login(self, event: ft.ControlEvent):
        self._login_handler.handle_login(event)

    def _on_signup(self, event: ft.ControlEvent):
        self._signup_handler.handle_signup(event)
