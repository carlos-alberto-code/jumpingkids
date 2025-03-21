from hexagon.application.repository import RoutinesRepositoryPort


class RoutinesRepositoryAdapter(RoutinesRepositoryPort):

    def get_all_routines(self) -> list:
        return super().get_all_routines()

    def get_exercises_by_routine_id(self, routine_id: int) -> list:
        return super().get_exercises_by_routine_id(routine_id)

    def get_favorite_routines_by_user_id(self, user_id: int) -> list:
        return super().get_favorite_routines_by_user_id(user_id)
