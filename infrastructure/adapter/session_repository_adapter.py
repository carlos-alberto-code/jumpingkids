from hexagon.domain.model import Child, Tutor
from hexagon.application.repository import SessionRepositoryPort

from infrastructure.persistence import Repository
from infrastructure.persistence.model import ChildEntity


class SessionRepositoryAdapter(SessionRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
        self._child_repository = Repository[ChildEntity](ChildEntity)
    
    def get_user(self, username: str, password: str) -> Tutor | Child | None:
        self._child_repository.get_by(ChildEntity.username == username)