from hexagon.domain.model import Tutor
from infrastructure.persistence.model.model import TutorEntity
from infrastructure.mapper.child_mapper import ChildMapper

class TutorMapper:

    def from_entity_to_domain(self, entity: TutorEntity) -> Tutor:
        return Tutor(
            id=entity.id,
            full_name=entity.full_name,
            children=[
                ChildMapper().from_entity_to_domain(child) for child in entity.children
            ]
        )

    def from_domain_to_entity(self, domain: Tutor) -> TutorEntity:
        return TutorEntity(
            id=domain.id,
            full_name=domain.full_name,
            children=[
                ChildMapper().from_domain_to_entity(child) for child in domain.children
            ]
        )
