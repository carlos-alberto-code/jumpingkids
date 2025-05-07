from domain.model import Child, Tutor, SubscriptionType, Routine
from infrastructure.database.model import ChildEntity, TutorEntity, SubscriptionTypeEntity, RoutineEntity

class LoginTutorMapper:
    @staticmethod
    def to_domain(entity: TutorEntity, map_children: bool = True) -> Tutor:
        return Tutor(
            id=entity.id,
            username=entity.username,
            password=entity.password,
            full_name=entity.full_name,
            children=[
                LoginChildMapper.to_domain(child, map_tutor=False)
                for child in entity.children
            ] if map_children else [],
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
    def to_domain(entity: ChildEntity, map_tutor: bool = True) -> Child:
        tutor_obj = LoginTutorMapper.to_domain(entity.tutor, map_children=False) if map_tutor else Tutor(
            id=0, username="", password="", full_name="", children=[], subscription_type=SubscriptionType(id=0, name="")
        )
        return Child(
            id=entity.id,
            username=entity.username,
            password=entity.password,
            full_name=entity.full_name,
            tutor=tutor_obj,
            favorite_routines=[
                Routine(
                    id=routine.id,
                    name=routine.name,
                    description=routine.description,
                    categories=[],  
                    exercises=[],
                    subscription_types=[]
                ) for routine in getattr(entity, 'favorite_routines', [])
            ]
        )
    
    @staticmethod
    def to_entity(child: Child) -> ChildEntity:
        if not child.tutor or not hasattr(child.tutor, 'id'):
            raise ValueError("Child must have a tutor with a valid id")
        return ChildEntity(
            full_name=child.full_name,
            tutor_id=child.tutor.id,
            username=child.username,
            password=child.password,
        )
