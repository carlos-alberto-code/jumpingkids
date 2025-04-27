from domain.login.model import Child, Tutor, SubscriptionType
from infrastructure.database.model import ChildEntity, TutorEntity, SubscriptionTypeEntity


class LoginTutorMapper:

    @staticmethod
    def to_domain(entity: TutorEntity) -> Tutor:
        return Tutor(
            id=entity.id,
            username=entity.username,
            password=entity.password,
            full_name=entity.full_name,
            children=[
                LoginChildMapper.to_domain(child)
                for child in entity.children
            ],
            subscription_type=(
                SubscriptionType.FREE if entity.subscription_type == "free"
                else SubscriptionType.PREMIUM
            )
        )
    

class LoginChildMapper:

    @staticmethod
    def to_domain(entity: ChildEntity) -> Child:
        return Child(
            id=entity.id,
            username=entity.username,
            password=entity.password,
            full_name=entity.full_name,
            tutor=LoginTutorMapper.to_domain(entity.tutor),
        )