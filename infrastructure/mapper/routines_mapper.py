from hexagon.domain.model import Routine
from infrastructure.persistence.model import RoutineEntity
from infrastructure.mapper.category_mapper import CategoryMapper
from infrastructure.mapper.exercise_mapper import ExerciseMapper

class RoutineMapper:
    
    def from_entity_to_domain(self, entity: RoutineEntity) -> Routine:
        return Routine(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            categories=[
                CategoryMapper().from_entity_to_domain(category) for category in entity.categories
            ],
            exercises=[
                ExerciseMapper().from_entity_to_domain(exercise) for exercise in entity.exercises
            ],
        )

    def from_domain_to_entity(self, domain: Routine) -> RoutineEntity:
        return RoutineEntity(
            id=domain.id,
            name=domain.name,
            description=domain.description,
            categories=[
                CategoryMapper().from_domain_to_entity(category) for category in domain.categories
            ],
            exercises=[
                ExerciseMapper().from_domain_to_entity(exercise) for exercise in domain.exercises
            ],
        )