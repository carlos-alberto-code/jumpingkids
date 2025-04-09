from domain.model.model import Exercise, Routine
from domain.application.repository import RoutinesRepositoryPort

from infrastructure.mapper import RoutineMapper
from infrastructure.mapper import ExerciseMapper
from infrastructure.persistence import Repository
from infrastructure.persistence.model import RoutineEntity


class RoutinesRepositoryAdapter(RoutinesRepositoryPort):

    def __init__(self) -> None:
        super().__init__()
        self._routine_mapper = RoutineMapper()
        self._exercise_mapper = ExerciseMapper()
        self._rutina_repository = Repository[RoutineEntity](RoutineEntity)

    def get_all_routines(self) -> list[Routine] | None:
        routine_entities = self._rutina_repository.get_all()
        if routine_entities:
            return [
                self._routine_mapper.from_entity_to_domain(routine_entity)
                for routine_entity in routine_entities
            ]
        return None

    def get_exercises_by_routine_id(self, routine_id: int) -> list[Exercise] | None:
        routine_entity = self._rutina_repository.get_by_id(routine_id)
        if routine_entity:
            return [
                self._exercise_mapper.from_entity_to_domain(exercise)
                for exercise in routine_entity.exercises
            ]
        return None

    def get_favorite_routines_by_user_id(self, user_id: int) -> list:
        return super().get_favorite_routines_by_user_id(user_id)
