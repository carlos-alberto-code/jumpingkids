import flet as ft

from domain.registration.registration_service_core import RegistrationServiceCore

from ui.app.components.snackbar import JSnackbar
from ui.app.auth.login.login_view import LoginView
from ui.app.auth.signup.payment_dialog import PaymentDialog
from ui.app.auth.signup.subscription_dialog import SubscriptionDialog
from ui.app.auth.signup.register_children_view import RegisterChildrenView

from infrastructure.repository import RegistrationRepositoryAdapter


class SignupHandler:
    def __init__(self, login_view: LoginView, page: ft.Page):
        self._login_view = login_view
        self._page = page

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
            snackbar = JSnackbar(
                message="Error al registrar el tutor: " + str(e),
                bgcolor=ft.Colors.GREY_100,
                text_color="#2D2242",
            )
            event.page.open(snackbar)
            return
        def on_finish_register_children(children_data):
            def on_subscription_selected(subscription_type):
                registration_service.set_subscription(subscription_type)
                if subscription_type == "premium":
                    def on_payment_success(payment_data):
                        registration_service.process_payment(payment_data)
                        registration_service.finalize_registration()
                        self._page.go("/tutor-app")
                        self._page.update()
                        self._page.close(payment_dialog)
                    payment_dialog = PaymentDialog(on_success=on_payment_success)
                    self._page.open(payment_dialog)
                else:
                    registration_service.finalize_registration()
                    snackbar = JSnackbar(
                        message="Registro exitoso. Ya puedes iniciar sesión.",
                        bgcolor=ft.Colors.GREY_100,
                        text_color="#2D2242",
                    )
                    event.page.open(snackbar)
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
        