from domain.auth.login.login_repository_port import LoginRepositoryPort
from domain.auth.login.login_service_port import LoginServicePort
from domain.model import Child, Tutor


class LoginServiceCore(LoginServicePort):

    def __init__(self, login_repository: LoginRepositoryPort) -> None:
        super().__init__()
        self._login_repository = login_repository
    
    def login(self, username: str, password: str) -> Tutor | Child | None:
        user = self._login_repository.get_by_username(username)
        return user if user else None
