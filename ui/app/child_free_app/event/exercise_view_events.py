import flet as ft

from ui.app.child_free_app.view.exercise_view import ExerciseView


class ExerciseViewEvents:

    def __init__(self, view: ExerciseView, services) -> None:
        self._view = view
        self._services = services
        
    def _on_play_click(self, event: ft.ControlEvent):
        button_play: ft.IconButton = event.control
    