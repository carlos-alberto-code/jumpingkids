from hexagon.domain.model import Routine
from infrastructure.persistence.model import RoutineEntity
from infrastructure.mapper.category_mapper import CategoryMapper
from infrastructure.mapper.exercise_mapper import ExerciseMapper


class RoutineMapper:
    
    @staticmethod
    def from_entity_to_domain(entity: RoutineEntity, include_categories=True) -> Routine:
        categories = []
        if include_categories:
            categories = [
                CategoryMapper.from_entity_to_domain(category, include_routines=False) 
                for category in entity.categories
            ]
            
        return Routine(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            categories=categories,
            exercises=[
                ExerciseMapper.from_entity_to_domain(exercise) for exercise in entity.exercises
            ],
        )

    @staticmethod
    def from_domain_to_entity(domain: Routine) -> RoutineEntity:
        return RoutineEntity(
            id=domain.id,
            name=domain.name,
            description=domain.description,
            categories=[
                CategoryMapper.from_domain_to_entity(category) for category in domain.categories
            ],
            exercises=[
                ExerciseMapper.from_domain_to_entity(exercise) for exercise in domain.exercises
            ],
        )