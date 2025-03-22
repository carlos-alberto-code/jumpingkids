import flet as ft

from ui.app_builder import AppViewBuilder


def main(page: ft.Page):
    page.title = "Rutinas"
    page.theme_mode = ft.ThemeMode.LIGHT

    app_builder = AppViewBuilder()
    page.views.extend(
        [view for view in app_builder.views]
    )
    page.update()


ft.app(target=main)
