import flet as ft

from domain.login import LoginServiceCore
from infrastructure.login import LoginRepositoryAdapter
from domain.subscription import SubscriptionServiceCore
from ui.subscription.subscription_gui_adapter import SubscriptionGuiAdapter


def main(page: ft.Page):

    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    user = LoginServiceCore(LoginRepositoryAdapter()).login("cabh", "cabh")
    print(user)

    if not user:
        raise ValueError("No se pudo iniciar sesión con las credenciales proporcionadas.")
    
    app = SubscriptionServiceCore(SubscriptionGuiAdapter()).get_user_app(user)
    
    page.theme = app.theme
    app_content = app.content
    page.add(app_content)


ft.app(target=main, port=9000)
