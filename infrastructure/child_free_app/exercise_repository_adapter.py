from domain.app.child_free_app.exercise.exercise_repository_port import ExerciseRepositoryPort

from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO

from infrastructure.repository import Repository
from infrastructure.database.model import ExerciseEntity, CategoryEntity, LevelEntity
from infrastructure.child_free_app.mapper import EXERCISE_MAPPER, CATEGORY_MAPPER, LEVEL_MAPPER


class ExerciseRepositoryAdapter(ExerciseRepositoryPort):

    def __init__(self) -> None:
        super().__init__()
        self._level_repository = Repository(LevelEntity)
        self._exercise_repository = Repository(ExerciseEntity)
        self._category_repository = Repository(CategoryEntity)

    def get_all_exercises(self) -> list[ExerciseDTO] | None:
        exercises = self._exercise_repository.get_all()
        if exercises:
            return [
                EXERCISE_MAPPER.TO_DTO(exercise)
                for exercise in exercises
            ]
        return None
    
    def get_all_categories(self) -> list[CategoryDTO] | None:
        categories = self._category_repository.get_all()
        if categories:
            return [
                CATEGORY_MAPPER.TO_DTO(category)
                for category in categories
            ]
        return None
    
    def get_all_levels(self) -> list[LevelDTO] | None:
        levels = self._level_repository.get_all()
        if levels:
            return [
                LEVEL_MAPPER.TO_DTO(level)
                for level in levels
            ]
        return None
    
    def filter_exercises_by_level(self, level_id: int) -> list[ExerciseDTO] | None:
        exercises = self._exercise_repository.get_by(ExerciseEntity.level_id == level_id)
        if isinstance(exercises, list):
            return [
                EXERCISE_MAPPER.TO_DTO(exercise)
                for exercise in exercises
            ]
        return None
    
    def filter_exercises_by_category(self, category_id: int) -> list[ExerciseDTO] | None:
        exercises = self._exercise_repository.get_by(ExerciseEntity.category_id == category_id)
        if isinstance(exercises, list):
            return [
                EXERCISE_MAPPER.TO_DTO(exercise)
                for exercise in exercises
            ]
        return None

    def search_exercises(self, text: str) -> list[ExerciseDTO] | None:
        print("Buscando ejercicios...")
    
    def add_favorite_exercise(self, child_id: int, exercise_id: int) -> None:
        print("Agregando ejercicio favorito...")
    
    def remove_favorite_exercise(self, child_id: int, exercise_id: int) -> None:
        print("Removiendo ejercicio favorito...")