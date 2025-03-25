import flet as ft

from hexagon.domain.model import Routine
from ui.view.layout import RoutinesViewLayout
    

class RoutinesView(ft.View):

    def __init__(self) -> None:
        super().__init__()
        self.router = "/routines"
        self._on_view_exercises_button_click = None
        self._on_favorite_button_click = None
        self._on_filter_by_favorite_button_click = None
        self._on_filter_by_category_button_click = None
        self._on_submit = None
        self._routines = []
        self.appbar = ft.AppBar(
            title=ft.Text("Rutinas"),
            automatically_imply_leading=False,
            center_title=True,
            elevation=5,
            actions=[
                ft.PopupMenuButton(
                    tooltip="Usuario",
                    icon=ft.Icons.ACCOUNT_CIRCLE,
                    elevation=5,
                    items=[
                        ft.PopupMenuItem(
                            text="Perfil",
                            icon=ft.Icons.PERSON,
                        ),
                        ft.PopupMenuItem(
                            text="Configuración",
                            icon=ft.Icons.SETTINGS,
                        ),
                        ft.PopupMenuItem(
                            text="Cerrar sesión",
                            icon=ft.Icons.LOGOUT,
                        ),
                    ],
                ),
                ft.Container(width=15)
            ]
        )
    
    @property
    def on_view_exercises_button_click(self):
        return self._on_view_exercises_button_click

    @on_view_exercises_button_click.setter
    def on_view_exercises_button_click(self, value):
        self._on_view_exercises_button_click = value

    @property
    def on_favorite_button_click(self):
        return self._on_favorite_button_click

    @on_favorite_button_click.setter
    def on_favorite_button_click(self, value):
        self._on_favorite_button_click = value

    @property
    def on_filter_by_favorite_button_click(self):
        return self._on_filter_by_favorite_button_click

    @on_filter_by_favorite_button_click.setter
    def on_filter_by_favorite_button_click(self, value):
        self._on_filter_by_favorite_button_click = value

    @property
    def on_filter_by_category_button_click(self):
        return self._on_filter_by_category_button_click

    @on_filter_by_category_button_click.setter
    def on_filter_by_category_button_click(self, value):
        self._on_filter_by_category_button_click = value
    
    @property
    def on_submit(self):
        return self._on_submit
    
    @on_submit.setter
    def on_submit(self, value):
        self._on_submit = value

    @property
    def routines(self):
        return self._routines
    
    @routines.setter
    def routines(self, routines: list[Routine]):
        self._routines = routines
        self.update_view(routines)
    
    def update_view(self, routines: list[Routine]) -> None:
        """
        Actualiza la vista con los nuevos datos de las rutinas.
        """
        layout = RoutinesViewLayout(
            routines,
            on_favorite_button_click=self._on_favorite_button_click,
            on_show_exercises_button_click=self._on_view_exercises_button_click,
            on_filter_by_favorites_button_click=self._on_filter_by_favorite_button_click,
            on_filter_by_category_button_click=self._on_filter_by_category_button_click,
            on_submit=self._on_submit,
        )
        self.controls = [layout]
