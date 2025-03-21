import flet as ft

from ui.view import RoutinesView
from ui.controller import RoutinesViewController
from hexagon.application.core import RoutinesServiceCore
from infrastructure.adapter import RoutinesRepositoryAdapter


class AppViewBuilder:

    def __init__(self) -> None:
        self._controller = RoutinesViewController(
            RoutinesServiceCore(RoutinesRepositoryAdapter()),
            RoutinesView()
        )

    @property
    def views(self) -> list[ft.View]:
        return [
            self._controller.view
        ]
