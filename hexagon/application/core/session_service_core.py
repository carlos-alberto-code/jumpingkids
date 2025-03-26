from hexagon.domain.model import Child, Tutor
from hexagon.application.service import SessionServicePort
from hexagon.application.repository import SessionRepositoryPort


class SessionServiceCore(SessionServicePort):

    def __init__(self, session_repository: SessionRepositoryPort) -> None:
        super().__init__()
        self._session_repository = session_repository
    
    def login(self, username: str, password: str) -> Tutor | Child | None:
        return self._session_repository.get_user(username, password)