import flet as ft
from domain.model.model import Exercise, Category, Level, SubscriptionType
from ui.app.child_free_app.components.exercise_view import (
    ProgressComponent,
    ExerciseListComponent,
    ExercisePlayerComponent
)

class ExerciseView(ft.View):
    def __init__(self, appbar: ft.AppBar | None = None) -> None:
        super().__init__(
            appbar=appbar,
            padding=10,
            scroll=ft.ScrollMode.AUTO,
        )
        
