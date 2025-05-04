import flet as ft

from domain.model import Tutor
from domain.login import LoginServiceCore
from domain.subscription import SubscriptionServiceCore

from infrastructure.login import LoginRepositoryAdapter

from ui.app_state import AppState
from ui.app.login.login_view import LoginView
from ui.app.components.sidebar import Sidebar
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter


def delete_slash(value: str) -> str:
    return value[1:] if value.startswith("/") else value


def show_snackbar_message(page: ft.Page, message: str, bgcolor: str, text_color: str) -> None:
    snackbar = ft.SnackBar(
        content=ft.Row(
            [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=bgcolor,
    )
    page.open(snackbar)


def main(page: ft.Page):

    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    
    sidebar = Sidebar()

    def on_login(event: ft.ControlEvent):
        if login_view.not_complet_data:
            show_snackbar_message(
                page=page,
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(login_view.username_field, login_view.password_field)

        if not user:
            show_snackbar_message(
                page=page,
                message="Usuario no encontrado!",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        # Solo si user existe, se ejecuta el resto
        subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())
        state = AppState(user=user, app=subscription_service.get_user_app(user))
        page.theme = state.app.theme
        sidebar.keys = {
            delete_slash(jview.name): jview.icon for jview in state.app.views.values()
        }
        page.views.clear()
        default_view = state.app.views["inicio"].view
        page.views.append(default_view)
        if (default_view.route):
            page.go(default_view.route)
        page.update()
    
    def on_signup(event: ft.ControlEvent):
        if login_view.not_signup_data:
            show_snackbar_message(
                page=page,
                message="Por favor, completa todos los campos.",
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            return

        tutor_data = {
            "username": login_view.signup.username,
            "password": login_view.signup.password,
            "full_name": login_view.signup.full_name,
        }
        from domain.registration.registration_service_core import RegistrationServiceCore
        from infrastructure.repository import RegistrationRepositoryAdapter
        from ui.app.register_children.register_children_view import RegisterChildrenView
        from ui.app.register_children.subscription_dialog import SubscriptionDialog
        from ui.app.register_children.payment_dialog import PaymentDialog

        registration_service = RegistrationServiceCore(RegistrationRepositoryAdapter())
        registration_service.start_registration(tutor_data)

        def on_finish_register_children(children_data):
            def on_subscription_selected(subscription_type):
                registration_service.set_subscription(subscription_type)
                if subscription_type == "premium":
                    def on_payment_success(payment_data):
                        registration_service.process_payment(payment_data)
                        registration_service.finalize_registration()
                        show_snackbar_message(
                            page=page,
                            message="¡Registro completo y pago exitoso!",
                            bgcolor=ft.Colors.GREEN_200,
                            text_color="#2D2242",
                        )
                        page.go("/tutor-app")
                        page.update()
                    page.dialog = PaymentDialog(on_success=on_payment_success)
                    page.dialog.open = True
                    page.update()
                else:
                    registration_service.finalize_registration()
                    show_snackbar_message(
                        page=page,
                        message="¡Registro completo! Bienvenido.",
                        bgcolor=ft.Colors.GREEN_200,
                        text_color="#2D2242",
                    )
                    page.go("/tutor-app")
                    page.update()
            page.dialog = SubscriptionDialog(on_select=on_subscription_selected)
            page.dialog.open = True
            page.update()

        register_children_view = RegisterChildrenView(
            on_finish=on_finish_register_children,
            registration_service=registration_service
        )
        page.views.append(register_children_view)
        page.go("/register-child")
        page.update()

    login_view = LoginView(
        on_login=on_login,
        on_signup=on_signup
    )

    page.views.append(login_view)
    page.go("/login")
    page.update()

ft.app(target=main, port=9000)
