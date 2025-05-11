from domain.app.child_free_app.exercise.exercise_service_port import ExerciseServicePort
from domain.manager.repository import Repository


class ExerciseServiceCore(ExerciseServicePort):
    
    def __init__(self, *repositories: Repository) -> None:
        super().__init__(*repositories)