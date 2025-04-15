from domain.model import Child, Tutor
from domain.application.repository import LoginRepositoryPort

from infrastructure.mapper import UserMapper
from infrastructure.persistence.repository import Repository
from infrastructure.persistence.model import ChildEntity, TutorEntity


class LoginRepositoryAdapter(LoginRepositoryPort):

    def __init__(self) -> None:
        super().__init__()
        self._child_repository = Repository[ChildEntity](ChildEntity)
        self._tutor_repository = Repository[TutorEntity](TutorEntity)

    def get_user_by_credentials(self, username: str, password: str) -> Tutor | Child | None:
        child_entity = self._child_repository.get_by(
            ChildEntity.username == username,
            ChildEntity.password == password,
        )
        if child_entity:
            child_mapper = UserMapper[Child](Child)
            return child_mapper.entity_to_domain(child_entity)

        tutor_entity = self._tutor_repository.get_by(
            TutorEntity.username == username,
            TutorEntity.password == password,
        )
        if tutor_entity:
            tutor_mapper = UserMapper[Tutor](Tutor)
            return tutor_mapper.entity_to_domain(tutor_entity)
        return None
