from application.service.routines_service_port import RoutinesServicePort
from domain.model import Exercise, Routine


class RoutinesServiceCore(RoutinesServicePort):

    def get_all_routines(self) -> list[Routine]:
        return super().get_all_routines()

    def get_exercises_by_routine_id(self, routine_id: int) -> list[Exercise]:
        return super().get_exercises_by_routine_id(routine_id)
    
    def get_favorite_routines_by_user_id(self, user_id: int) -> list[Routine]:
        return super().get_favorite_routines_by_user_id(user_id)
    
    def get_routines_by_category_id(self, category_id: int) -> list[Routine]:
        return super().get_routines_by_category_id(category_id)
    
    def add_routine_to_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        return super().add_routine_to_user_favorite_list(user_id, routine_id)
    
    def remove_routine_from_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        return super().remove_routine_from_user_favorite_list(user_id, routine_id)
