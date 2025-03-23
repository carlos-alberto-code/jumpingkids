from hexagon.domain.model import Child
from infrastructure.mapper.tutor_mapper import TutorMapper
from infrastructure.persistence.model.model import ChildEntity

class ChildMapper:

    @staticmethod
    def from_entity_to_domain(entity: ChildEntity) -> Child:
        return Child(
            id=entity.id,
            full_name=entity.full_name,
            age=entity.age,
            tutor=TutorMapper().from_entity_to_domain(entity.tutor)
        )

    @staticmethod
    def from_domain_to_entity(domain: Child) -> ChildEntity:
        return ChildEntity(
            id=domain.id,
            full_name=domain.full_name,
            age=domain.age,
            tutor=TutorMapper().from_domain_to_entity(domain.tutor)
        )
