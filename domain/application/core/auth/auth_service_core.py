from domain.model.model import User, Tutor, Child, Nutritionist
from domain.application.service.auth.auth_service_port import AuthServicePort
from domain.application.repository.auth.auth_repository_port import AuthRepositoryPort


class AuthServiceCore(AuthServicePort):
    def __init__(self, auth_repository_port: AuthRepositoryPort):
        self._auth_repository_port = auth_repository_port
        super().__init__()
    
    def login(self, username: str, password: str) -> Tutor | Child | Nutritionist | None:
        return self._auth_repository_port.get_user(username, password)
    