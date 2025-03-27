import flet as ft

from ui.app_builder import AppViewBuilder


def main(page: ft.Page):
    page.title = "Rutinas"
    page.theme_mode = ft.ThemeMode.LIGHT

    app_builder = AppViewBuilder()
    for route, view in app_builder:
        page.views.append(view)
    
    page.update()


ft.app(target=main)
