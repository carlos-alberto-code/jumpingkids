from hexagon.domain.model import Category
from infrastructure.persistence.model.model import CategoryEntity


class CategoryMapper:

    def from_entity_to_domain(self, entity: CategoryEntity) -> Category:
        return Category(
            id=entity.id,
            name=entity.name,
        )

    def from_domain_to_entity(self, domain: Category) -> CategoryEntity:
        return CategoryEntity(
            id=domain.id,
            name=domain.name,
        )
    