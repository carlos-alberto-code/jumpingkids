from domain.model import Child, Tutor
from domain.auth.signup.signup_service_port import SignupServicePort
from domain.auth.signup.signup_repository_port import SignupRepositoryPort


class SignupServiceCore(SignupServicePort):
    def __init__(self, repository: SignupRepositoryPort):
        self._repository = repository

    def add_child(self, child: Child):
        ...
    
    def add_tutor(self, tutor: Tutor):
        ...
    
    def tutor_exists(self, username: str) -> bool:
        ...
