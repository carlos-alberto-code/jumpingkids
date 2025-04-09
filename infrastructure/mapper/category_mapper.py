from domain.model.model import Category
from infrastructure.persistence.model.model import CategoryEntity


class CategoryMapper:

    @staticmethod
    def from_entity_to_domain(entity: CategoryEntity, include_routines=True) -> Category:
        # Importación local para evitar la circular
        from infrastructure.mapper.routines_mapper import RoutineMapper
        
        # Evitamos la recursión infinita
        routines = []
        if include_routines:
            routines = [
                RoutineMapper.from_entity_to_domain(routine, include_categories=False) 
                for routine in entity.routines
            ]
            
        return Category(
            id=entity.id,
            name=entity.name,
            routines=routines
        )

    @staticmethod
    def from_domain_to_entity(domain: Category) -> CategoryEntity:
        return CategoryEntity(
            id=domain.id,
            name=domain.name,
        )
