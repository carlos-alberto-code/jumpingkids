from domain.model.model import Child
from domain.application.repository import SessionRepositoryPort

from infrastructure.mapper import ChildMapper
from infrastructure.persistence import Repository
from infrastructure.persistence.model import ChildEntity


class ChildSessionRepositoryAdapter(SessionRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
        self._child_repository = Repository[ChildEntity](ChildEntity)
    
    def get_user(self, username: str) -> Child | None:
        child = self._child_repository.get_by(ChildEntity.username == username)
        return ChildMapper.from_entity_to_domain(child) if child else None
