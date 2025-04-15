from domain.model.model import Tutor, Child
from domain.application.service import LoginServicePort
from domain.application.repository import LoginRepositoryPort


class LoginServiceCore(LoginServicePort):

    def __init__(self, login_repository: LoginRepositoryPort) -> None:
        super().__init__(login_repository)
    
    def login(self, username: str, password: str) -> Tutor | Child | None:
        return self._login_repository.get_user_by_credentials(username, password)
    