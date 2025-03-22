from hexagon.domain.model import Exercise, Routine
from hexagon.application.repository import RoutinesRepositoryPort
from hexagon.application.service.routines_service_port import RoutinesServicePort


class RoutinesServiceCore(RoutinesServicePort):

    def __init__(self, routines_repository_port: RoutinesRepositoryPort) -> None:
        super().__init__()
        self._routines_repository = routines_repository_port

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
