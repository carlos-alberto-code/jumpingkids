from hexagon.domain.model import Child
from infrastructure.persistence.model.model import ChildEntity
from infrastructure.mapper.tutor_mapper import TutorMapper

class ChildMapper:

    def from_entity_to_domain(self, entity: ChildEntity) -> Child:
        return Child(
            id=entity.id,
            full_name=entity.full_name,
            age=entity.age,
            tutor=TutorMapper().from_entity_to_domain(entity.tutor)
        )

    def from_domain_to_entity(self, domain: Child) -> ChildEntity:
        return ChildEntity(
            id=domain.id,
            full_name=domain.full_name,
            age=domain.age,
            tutor=TutorMapper().from_domain_to_entity(domain.tutor)
        )
