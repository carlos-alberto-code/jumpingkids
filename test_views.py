import flet as ft

from domain.subscription.susbcription_service_core import SubscriptionServiceCore
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter
from ui.app.login.login_view import LoginView
from domain.login.login_service_core import LoginServiceCore
from infrastructure.login.login_repository_adapter import LoginRepositoryAdapter


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def on_login(event: ft.ControlEvent):
        print("Login button clicked")
    
    def on_signup(event: ft.ControlEvent):
        print("Signup button clicked")

    login_view = LoginView(
        on_login=on_login,
        on_signup=on_signup
    )

    page.views.append(login_view)
    page.go("/login")
    page.update()

ft.app(main)