from domain.model.model import Child
from infrastructure.persistence.model.model import ChildEntity

class ChildMapper:

    @staticmethod
    def from_entity_to_domain(entity: ChildEntity, include_tutor=True, include_favorite_routines=True) -> Child:
        # Importación local para evitar la circular
        from infrastructure.mapper import TutorMapper
        from infrastructure.mapper.routines_mapper import RoutineMapper
        
        tutor = None
        if include_tutor and entity.tutor is not None:
            tutor = TutorMapper.from_entity_to_domain(entity.tutor, include_children=False)
        
        favorite_routines = []
        if include_favorite_routines and hasattr(entity, 'favorite_routines') and entity.favorite_routines is not None:
            favorite_routines = [
                RoutineMapper.from_entity_to_domain(routine, include_categories=False) for routine in entity.favorite_routines
            ]
        
        return Child(
            id=entity.id,
            full_name=entity.full_name,
            username=entity.username,
            password=entity.password,
            tutor=tutor,
            favorite_routines=favorite_routines
        )

    @staticmethod
    def from_domain_to_entity(model: Child, include_tutor=False, include_favorite_routines=False) -> ChildEntity:
        # Importación local para evitar la circular
        from infrastructure.mapper import TutorMapper
        from infrastructure.mapper.routines_mapper import RoutineMapper
        
        child_entity = ChildEntity(
            id=model.id,
            full_name=model.full_name,
            username=model.username,
            password=model.password,
            tutor_id=model.tutor.id if model.tutor else None
        )
        
        # Solo mapear el tutor si se solicita explícitamente y existe
        if include_tutor and model.tutor:
            tutor_entity = TutorMapper.from_domain_to_entity(model.tutor, include_children=False)
            child_entity.tutor = tutor_entity
        
        # Solo mapear las rutinas favoritas si se solicita explícitamente y existen
        if include_favorite_routines and model.favorite_routines:
            child_entity.favorite_routines = [
                RoutineMapper.from_domain_to_entity(routine, include_categories=False, include_exercises=False) 
                for routine in model.favorite_routines
            ]
            
        return child_entity
