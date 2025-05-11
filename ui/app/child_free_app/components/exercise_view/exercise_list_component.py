import flet as ft

from ui.app.child_free_app.components.exercise_view.exercise_card import ExerciseCard
from domain.model.dto import ExerciseDTO

class ExerciseList(ft.ListView):
    
    def __init__(self, exercises: list[ExerciseDTO], on_exercise_select=None):
        self._exercises = exercises
        self._on_exercise_selected = on_exercise_select
        
        super().__init__(
            controls=[
                ExerciseCard(
                    exercise=exercise,
                    on_click=self._on_exercise_selected
                ) for exercise in self._exercises
            ],
        )
    
    @property
    def exercises(self):
        return self._exercises
    
    @exercises.setter
    def exercises(self, exercises: list[ExerciseDTO]):
        self._exercises = exercises
        self.controls = [
            ExerciseCard(
                exercise=exercise,
                on_click=self._on_exercise_selected
            ) for exercise in self._exercises
        ] 
