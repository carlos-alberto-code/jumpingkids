from domain.model.model import SubscriptionType
from domain.command.model import TutorCreate
from domain.auth.signup.signup_repository_port import SignupRepositoryPort

from infrastructure.repository import Repository
from infrastructure.auth.signup.tutor_mapper import TutorMapper
from infrastructure.database.model import TutorEntity, SubscriptionTypeEntity
from infrastructure.auth.signup.subscription_mapper import SubscriptionTypeMapper


class SignupRepositoryAdapter(SignupRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
        self._repository = Repository(TutorEntity)
        self._subscription_type_repository = Repository(SubscriptionTypeEntity)

    def save_tutor(self, tutor: TutorCreate):
        tutor_entity = TutorMapper.to_entity(tutor)
        self._repository.add(tutor_entity)
    
    def tutor_exists(self, username: str) -> bool:
        return self._repository.exists(TutorEntity.username == username)
    
    def get_subscription_types(self) -> list[SubscriptionType] | None:
        entities = self._subscription_type_repository.get_all()
        return [
            SubscriptionTypeMapper.to_domain(entity)
            for entity in entities
        ] if entities else None
