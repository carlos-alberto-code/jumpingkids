import flet as ft

from domain.model import Exercise, Routine
from ui.kids.view.layout import RoutinesViewLayout
    

class RoutinesView(ft.View):

    def __init__(self, appbar: ft.AppBar, navigation: ft.NavigationBar) -> None:
        super().__init__()
        self.router = "/routines"
        self._on_view_exercises_button_click = None
        self._on_favorite_button_click = None
        self._on_filter_by_favorite_button_click = None
        self._on_filter_by_category_button_click = None
        self._on_submit = None
        self._routines = []
        self._exercises = []
        self._layout: RoutinesViewLayout | None = None
        self.appbar = appbar
        self.navigation_bar = navigation
    
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
    def routines(self) -> list[Routine]:
        return self._routines
    
    @routines.setter
    def routines(self, routines: list[Routine]):
        self._routines = routines
        self.update_view(routines)
    
    def update_view(self, routines: list[Routine]) -> None:
        """
        Actualiza la vista con los nuevos datos de las rutinas. Verifica si las rutinas están marcadas como favoritas para cambiar el icono del botón de favoritos de forma que se muestre marcado.
        """
        self._layout = RoutinesViewLayout(
            routines,
            on_favorite_button_click=self._on_favorite_button_click,
            on_show_exercises_button_click=self._on_view_exercises_button_click,
            on_filter_by_favorites_button_click=self._on_filter_by_favorite_button_click,
            on_filter_by_category_button_click=self._on_filter_by_category_button_click,
            on_submit=self._on_submit,
        )
        self.controls = [self._layout]
    
    @property
    def exercises(self) -> list[Exercise]:
        return self._exercises
    
    @exercises.setter
    def exercises(self, exercises: list[Exercise]) -> None:
        self._exercises = exercises
        print("Logica para mostrar ejercicios en la vista")
        # Aquí puedes agregar lógica para mostrar los ejercicios en la vista si es necesario.
        # Por ejemplo, podrías actualizar un componente de la interfaz de usuario para mostrar los ejercicios.

