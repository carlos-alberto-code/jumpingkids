from domain.model import Exercise, Routine
from application.repository import RoutinesRepositoryPort
from application.service.routines_service_port import RoutinesServicePort
from infrastructure.repository.routines_repository_adapter import RoutinesRepositoryAdapter


class RoutinesServiceCore(RoutinesServicePort):

    def __init__(self) -> None:
        super().__init__()
        self._routines_repository: RoutinesRepositoryPort = RoutinesRepositoryAdapter()

    def get_all_routines(self) -> list[Routine]:
        routines: list[Routine] = self._routines_repository.get_all_routines()
        return routines

    def get_exercises_by_routine_id(self, routine_id: int) -> list[Exercise]:
        exercises: list[Exercise] = self._routines_repository.get_exercises_by_routine_id(routine_id)
        return exercises
    
    def get_favorite_routines_by_user_id(self, user_id: int) -> list[Routine]:
        routines: list[Routine] = self._routines_repository.get_favorite_routines_by_user_id(user_id)
        return routines
    
    def get_routines_by_category_id(self, category_id: int) -> list[Routine]:
        return super().get_routines_by_category_id(category_id)
    
    def add_routine_to_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        return super().add_routine_to_user_favorite_list(user_id, routine_id)
    
    def remove_routine_from_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        return super().remove_routine_from_user_favorite_list(user_id, routine_id)
