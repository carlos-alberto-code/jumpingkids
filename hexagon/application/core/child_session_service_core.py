from hexagon.domain.model import Child, Tutor
from hexagon.application.service import ChildSessionServicePort
from hexagon.application.repository import SessionRepositoryPort


class ChildSessionServiceCore(ChildSessionServicePort):

    def __init__(self, session_repository: SessionRepositoryPort) -> None:
        super().__init__()
        self._session_repository = session_repository
    
    def login(self, username: str) -> Child | None:
        return self._session_repository.get_user(username)