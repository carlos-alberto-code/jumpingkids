import flet as ft

from domain.manager.event import ViewEvent
from domain.manager.service import Service
from ui.app.child_free_app.view.exercise_view import ExerciseView


class ExerciseViewEvent(ViewEvent):

    def __init__(self, exercise_view: ExerciseView, services: list[Service]) -> None:
        super().__init__(exercise_view, services)
        self._exercise_service: ExerciseServicePort = services[0]
    
    def _connect_events(self) -> None:
        self._view.on_submit = self._on_submit
        self._view.on_filter_by_level = self._on_filter_by_level
        self._view.on_filter_by_category = self._on_filter_by_category
        self._view.on_view_exercise_details = self._on_view_exercise_details
        self._view.on_favorite_exercise_click = self._on_favorite_exercise_click
        
    def _on_submit(self, e: ft.ControlEvent):
        ...
    
    def _on_filter_by_level(self, e: ft.ControlEvent):
        ...

    def _on_filter_by_category(self, e: ft.ControlEvent):
        ...
    
    def _on_view_exercise_details(self, e: ft.ControlEvent):
        ...
    
    def _on_favorite_exercise_click(self, e: ft.ControlEvent):
        ...
    