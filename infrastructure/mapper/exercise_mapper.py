from hexagon.domain.model import Exercise
from infrastructure.persistence.model.model import ExerciseEntity


class ExerciseMapper:

    def from_entity_to_domain(self, entity: ExerciseEntity) -> Exercise:
        return Exercise(
            id=entity.id,
            name=entity.name,
            description=entity.description,
        )

    def from_domain_to_entity(self, domain: Exercise) -> ExerciseEntity:
        return ExerciseEntity(
            id=domain.id,
            name=domain.name,
            description=domain.description,
        )
