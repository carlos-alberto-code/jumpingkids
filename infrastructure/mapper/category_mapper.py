from hexagon.domain.model import Category
from infrastructure.mapper.routines_mapper import RoutineMapper
from infrastructure.persistence.model.model import CategoryEntity


class CategoryMapper:

    def from_entity_to_domain(self, entity: CategoryEntity) -> Category:
        return Category(
            id=entity.id,
            name=entity.name,
            routines=[
                RoutineMapper().from_entity_to_domain(routine) for routine in entity.routines
            ]
        )

    def from_domain_to_entity(self, domain: Category) -> CategoryEntity:
        return CategoryEntity(
            id=domain.id,
            name=domain.name,
        )
    