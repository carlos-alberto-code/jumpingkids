import flet as ft

from domain.login import LoginServiceCore
from domain.subscription import SubscriptionServiceCore

from infrastructure.login import LoginRepositoryAdapter

from ui.app.login.login_view import LoginView
from ui.adapter.subscription_gui_adapter import SubscriptionGuiAdapter

from app_state import AppState


def show_snackbar_message(page: ft.Page, message: str, color: str, duration: int = 4000) -> None:
    snackbar = ft.SnackBar(
        content=ft.Text(message),
        bgcolor=color,
        duration=duration
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
                color=ft.Colors.RED
            )

        login_service = LoginServiceCore(LoginRepositoryAdapter())
        user = login_service.login(login_view.username_field, login_view.password_field)

        if not user:
            show_snackbar_message(
                page=page,
                message="Usuario no encontrado!",
                color=ft.Colors.RED
            )

        if user:
            subscription_service = SubscriptionServiceCore(SubscriptionGuiAdapter())
            state = AppState(user=user, app=subscription_service.get_user_app(user))
    
        page.theme = state.app.theme
        sidebar.keys = state.app.views.names

        page.views.clear()
        default_view_name = state.app.views.names[0]
        default_view = state.app.views[default_view_name]
        page.views.append(default_view)
        page.go(default_view.route)
        page.update()
    
    def on_signup(event: ft.ControlEvent):
        print("Signup button clicked")

    login_view = LoginView(
        on_login=on_login,
        on_signup=on_signup
    )

    page.views.append(login_view)
    page.go("/login")
    page.update()

ft.app(target=main, port=9000)
