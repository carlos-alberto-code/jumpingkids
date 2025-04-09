from domain.model.model import Child, Tutor
from application.service import ChildSessionServicePort
from application.repository import SessionRepositoryPort


class ChildSessionServiceCore(ChildSessionServicePort):

    def __init__(self, child_session_repository: SessionRepositoryPort) -> None:
        super().__init__()
        self._session_repository = child_session_repository
    
    def login(self, username: str) -> Child | None:
        return self._session_repository.get_user(username)