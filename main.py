import flet as ft

from view import RoutinesView
from controller import RoutinesViewController
from hexagon.application.core import RoutinesServiceCore
from infrastructure.adapter import RoutinesRepositoryAdapter


routines_view_controller = RoutinesViewController(
    RoutinesServiceCore(RoutinesRepositoryAdapter()),
    RoutinesView()
)

def main(page: ft.Page):
    page.title = "Rutinas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.views.append(
        routines_view_controller.view
    )
    page.update()

ft.app(target=main, view=ft.AppView.FLET_APP_WEB)