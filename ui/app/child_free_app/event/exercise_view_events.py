import flet as ft

from ui.app.child_free_app.dto import ExerciseDTO
from ui.app.child_free_app.view.exercise_view import ExerciseView


class ExerciseViewEvents:

    def __init__(self, view: ExerciseView, exercise_service: ExerciseServicePort) -> None:
        self._view = view
        self._exercise_service = exercise_service
        self._connect()
    
    def _connect(self):
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
    