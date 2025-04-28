from domain.model import Child, Tutor, SubscriptionType
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
            subscription_type=SubscriptionType(
                id=entity.subscription_type_id,
                name=entity.subscription_type.name
            )
        )

    @staticmethod
    def to_entity(tutor: Tutor) -> TutorEntity:
        return TutorEntity(
            full_name=tutor.full_name,
            username=tutor.username,
            password=tutor.password,
            subscription_type_id=tutor.subscription_type.id,
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
    
    @staticmethod
    def to_entity(child: Child) -> ChildEntity:
        return ChildEntity(
            full_name=child.full_name,
            tutor_id=child.tutor.id,
            username=child.username,
            password=child.password,
        )
    