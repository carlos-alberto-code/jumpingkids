from abc import abstractmethod

from interface.crud.read import GetAll

from domain.manager.service import Service
from domain.manager.repository import Repository

from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO


class ExerciseServicePort(
    Service,
    GetAll[ExerciseDTO]
):

    def __init__(self, *repositories: Repository) -> None:
        super().__init__(*repositories)
    
    @abstractmethod
    def get_categories(self) -> list[CategoryDTO]| None: pass

    @abstractmethod
    def get_levels(self) -> list[LevelDTO] | None: pass

    @abstractmethod
    def search(self, text: str) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def filter_by_level_id(self, level_id: int) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def filter_by_category_id(self, category_id: int) -> list[ExerciseDTO] | None: pass

    @abstractmethod
    def add_favorite_exercise(self, user_id: int, exercise_id: int) -> None: pass

    @abstractmethod
    def remove_favorite_exercise(self, user_id: int, exercise_id: int) -> None: pass
    