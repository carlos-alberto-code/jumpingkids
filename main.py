import flet as ft
from ui.controllers.auth_controller import AuthController

def main(page: ft.Page):

    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    auth_controller = AuthController(page)
    auth_controller.show_login_view()

ft.app(target=main, port=9000)
