from abc import abstractmethod

from domain.manager.repository import Repository

from interface.crud.read import GetAll
from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO


class ExerciseRepositoryPort(Repository):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def get_all_exercises(self) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def get_all_categories(self) -> list[CategoryDTO] | None: pass

    @abstractmethod
    def get_all_levels(self) -> list[LevelDTO] | None: pass

    @abstractmethod
    def search_exercises(self, text: str) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def filter_exercises_by_level(self, level_id: int) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def filter_exercises_by_category(self, category_id: int) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def add_favorite_exercise(self, child_id:int, exercise_id: int) -> None: pass

    @abstractmethod
    def remove_favorite_exercise(self, child_id:int, exercise_id: int) -> None: pass
    