from domain.command.model import TutorCreate
from domain.auth.signup.signup_repository_port import SignupRepositoryPort

from infrastructure.repository import Repository
from infrastructure.database.model import TutorEntity
from infrastructure.auth.signup.signup_mapper import TutorMapper


class SignupRepositoryAdapter(SignupRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
        self._repository = Repository(TutorEntity)

    def save_tutor(self, tutor: TutorCreate):
        tutor_entity = TutorMapper.to_entity(tutor)
        self._repository.add(tutor_entity)
    
    def tutor_exists(self, username: str) -> bool:
        return self._repository.exists(TutorEntity.username == username)
