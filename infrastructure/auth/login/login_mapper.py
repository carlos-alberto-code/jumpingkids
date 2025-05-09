from domain.model.model import Child, Tutor, SubscriptionType, Routine
from infrastructure.database.model import ChildEntity, TutorEntity

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
