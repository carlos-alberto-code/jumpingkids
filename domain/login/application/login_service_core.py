from domain.login.model import Child, Tutor
from domain.login.application.login_service_port import LoginServicePort
from domain.login.application.login_repository_port import LoginRepositoryPort


class LoginServiceCore(LoginServicePort):

    def __init__(self, login_repository: LoginRepositoryPort) -> None:
        super().__init__()
        self._login_repository = login_repository
    
    def login(self, username: str, password: str) -> Tutor | Child | None:
        user = self._login_repository.get_by_username(username)
        return user if user else None

    def signup(self, user: Tutor | Child) -> None:
        self._login_repository.create_user(user)
        
