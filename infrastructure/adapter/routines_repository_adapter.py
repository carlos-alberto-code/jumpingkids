from hexagon.domain.model import Exercise, Routine
from hexagon.application.repository import RoutinesRepositoryPort

from infrastructure.persistence import Repository
from infrastructure.persistence.model import RoutineEntity
from infrastructure.mapper.routines_mapper import RoutineMapper
from infrastructure.mapper.exercise_mapper import ExerciseMapper


class RoutinesRepositoryAdapter(RoutinesRepositoryPort):

    def __init__(self) -> None:
        super().__init__()
        self._routine_mapper = RoutineMapper()
        self._exercise_mapper = ExerciseMapper()
        self._rutina_repository = Repository[RoutineEntity](RoutineEntity)

    def get_all_routines(self) -> list[Routine]:
        routine_entities = self._rutina_repository.get_all()
        return [
            self._routine_mapper.from_entity_to_domain(routine_entity)
            for routine_entity in routine_entities
        ]

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
