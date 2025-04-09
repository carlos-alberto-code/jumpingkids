from domain.model.model import Tutor
from infrastructure.persistence.model.model import TutorEntity
from infrastructure.mapper.child_mapper import ChildMapper


class TutorMapper:

    @staticmethod
    def from_entity_to_domain(entity: TutorEntity, include_children=True) -> Tutor:
        children = []
        if include_children:
            # Importación local para evitar la circular
            from infrastructure.mapper.child_mapper import ChildMapper
            children = [
                ChildMapper.from_entity_to_domain(child, include_tutor=False, include_favorite_routines=False) 
                for child in entity.children
            ]
        
        return Tutor(
            id=entity.id,
            full_name=entity.full_name,
            username=entity.username,
            password=entity.password,
            children=children
        )

    @staticmethod
    def from_domain_to_entity(domain: Tutor, include_children=True) -> TutorEntity:
        tutor_entity = TutorEntity(
            id=domain.id,
            full_name=domain.full_name,
            username=domain.username,
            password=domain.password
        )
        
        # Solo mapear los hijos si se solicita explícitamente
        if include_children and domain.children:
            from infrastructure.mapper.child_mapper import ChildMapper
            tutor_entity.children = [
                ChildMapper.from_domain_to_entity(child, include_tutor=False, include_favorite_routines=False) 
                for child in domain.children
            ]
            
        return tutor_entity
