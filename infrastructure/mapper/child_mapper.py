from hexagon.domain.model import Child
from infrastructure.persistence.model.model import ChildEntity

class ChildMapper:

    @staticmethod
    def from_entity_to_domain(entity: ChildEntity) -> Child:
        # Importación local para evitar la circular
        from infrastructure.mapper import TutorMapper
        from infrastructure.mapper.routines_mapper import RoutineMapper
        
        return Child(
            id=entity.id,
            full_name=entity.full_name,
            age=entity.age,
            tutor=TutorMapper.from_entity_to_domain(entity.tutor),
            favorite_routines=[
                RoutineMapper.from_entity_to_domain(routine) for routine in entity.favorite_routines
            ]
        )

    @staticmethod
    def from_domain_to_entity(domain: Child) -> ChildEntity:
        # Importación local para evitar la circular
        from infrastructure.mapper import TutorMapper
        from infrastructure.mapper.routines_mapper import RoutineMapper
        
        return ChildEntity(
            id=domain.id,
            full_name=domain.full_name,
            age=domain.age,
            tutor=TutorMapper.from_domain_to_entity(domain.tutor)
        )
