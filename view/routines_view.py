import flet as ft

from hexagon.domain.model import Routine


class RoutinesView(ft.View):

    def __init__(
            self,
            on_view_exercises_button_click=None,
            on_favorite_button_click=None,
            on_filter_by_favorite_button_click=None,
            on_filter_by_category_button_click=None,
    ) -> None:
        super().__init__()
        self._on_view_exercises_button_click = on_view_exercises_button_click
        self._on_favorite_button_click = on_favorite_button_click
        self._on_filter_by_favorite_button_click = on_filter_by_favorite_button_click
        self._on_filter_by_category_button_click = on_filter_by_category_button_click
        self._routines = []
    
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
    def routines(self):
        return self._routines
    
    @routines.setter
    def routines(self, routines: list[Routine]):
        self._routines = routines