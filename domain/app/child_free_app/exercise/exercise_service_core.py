from domain.manager.repository import Repository
from domain.app.child_free_app.exercise.exercise_service_port import ExerciseServicePort

from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO
from infrastructure.child_free_app.exercise_repository_adapter import ExerciseRepositoryAdapter


class ExerciseServiceCore(ExerciseServicePort):
    
    def __init__(self, *repositories: Repository) -> None:
        super().__init__(*repositories)
        self._repository = self._get_repository(ExerciseRepositoryAdapter)
    
    def get_all(self) -> list[ExerciseDTO] | None:
        return self._repository.get_all_exercises()
    
    def get_categories(self) -> list[CategoryDTO] | None:
        return self._repository.get_all_categories()
    
    def get_levels(self) -> list[LevelDTO] | None:
        return self._repository.get_all_levels()
    
    
    def filter_by_category_id(self, category_id: int) -> list[ExerciseDTO] | None:
        return self._repository.filter_exercises_by_category(category_id)
    
    def filter_by_level_id(self, level_id: int) -> list[ExerciseDTO] | None:
        return self._repository.filter_exercises_by_level(level_id)
    
    def search(self, text: str) -> list[ExerciseDTO] | None:
        print("Buscando...")
        # TODO: Implementar la búsqueda de ejercicios por nombre

    def add_favorite_exercise(self, user_id: int, exercise_id: int) -> None:
        print("Agregando ejercicio favorito...")
        # TODO: Implementar la lógica para agregar un ejercicio a favoritos
    
    def remove_favorite_exercise(self, user_id: int, exercise_id: int) -> None:
        print("Removiendo ejercicio favorito...")
        # TODO: Implementar la lógica para eliminar un ejercicio de favoritos
