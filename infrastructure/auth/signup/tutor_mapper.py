from domain.model.command import TutorCreate
from infrastructure.database.model import TutorEntity

class TutorMapper:

    @staticmethod
    def to_entity(tutor: TutorCreate) -> TutorEntity:
        entity = TutorEntity(
            full_name=tutor.full_name,
            username=tutor.username,
            password=tutor.password,
            subscription_type_id=tutor.subscription_type_id
        )
        return entity
