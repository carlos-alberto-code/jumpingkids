from domain.model.model import SubscriptionType
from infrastructure.database.model import SubscriptionTypeEntity


class SubscriptionTypeMapper:

    @staticmethod
    def to_domain(entity: SubscriptionTypeEntity) -> SubscriptionType:
        return SubscriptionType(
            id=entity.id,
            name=entity.name,
        )