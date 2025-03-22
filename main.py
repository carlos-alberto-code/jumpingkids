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
    page.views.append(
        routines_view_controller.view
    )

ft.app(target=main)