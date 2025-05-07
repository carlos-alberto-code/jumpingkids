from domain.command.model import TutorCreate
from domain.auth.signup.signup_service_port import SignupServicePort
from domain.auth.signup.signup_repository_port import SignupRepositoryPort


class SignupServiceCore(SignupServicePort):
    def __init__(self, repository: SignupRepositoryPort):
        self._repository = repository
    
    def add_tutor(self, tutor: TutorCreate):
        self._repository.save_tutor(tutor)
    
    def tutor_exists(self, username: str) -> bool:
        return self._repository.tutor_exists(username)
