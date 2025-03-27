import flet as ft

from ui.app_builder import AppViewBuilder
from ui.view.theme import JumpingKidsTheme


def main(page: ft.Page):

    page.theme = JumpingKidsTheme()
    page.theme_mode = ft.ThemeMode.LIGHT

    app_builder = AppViewBuilder()
    page.views.extend(view for _, view in app_builder)
    page.update()


ft.app(target=main)
