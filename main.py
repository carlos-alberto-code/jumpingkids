import flet as ft

from ui.theme.child_free_theme import ChildFreeTheme
from ui.app.auth.controllers.auth_controller import AuthController


def main(page: ft.Page):

    page.padding = 0
    page.theme = ChildFreeTheme()
    page.theme_mode = ft.ThemeMode.LIGHT
    
    auth_controller = AuthController(page)
    auth_controller.show_auth_view()


ft.app(target=main, port=9000)
