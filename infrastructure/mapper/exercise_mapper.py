from hexagon.domain.model import Exercise
from infrastructure.persistence.model.model import ExerciseEntity


class ExerciseMapper:

    @staticmethod
    def from_entity_to_domain(entity: ExerciseEntity) -> Exercise:
        return Exercise(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )

    @staticmethod
    def from_domain_to_entity(domain: Exercise) -> ExerciseEntity:
        return ExerciseEntity(
            id=domain.id,
            name=domain.name,
            description=domain.description,
        )
