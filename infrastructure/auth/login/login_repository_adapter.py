from domain.model import Child, Tutor
from domain.login import LoginRepositoryPort

from infrastructure.repository import Repository
from infrastructure.login.login_mapper import LoginTutorMapper
from infrastructure.login.login_mapper import LoginChildMapper
from infrastructure.database.model import ChildEntity, TutorEntity


class LoginRepositoryAdapter(LoginRepositoryPort):

    def __init__(self) -> None:
        super().__init__()
        self._tutot_repository = Repository[TutorEntity](TutorEntity)
        self._child_repository = Repository[ChildEntity](ChildEntity)
    
    def get_by_username(self, username: str) -> Tutor | Child | None:
        tutor = self._tutot_repository.get_by(TutorEntity.username == username)
        if tutor:
            return LoginTutorMapper.to_domain(tutor)
        child = self._child_repository.get_by(ChildEntity.username == username)
        if child:
            return LoginChildMapper.to_domain(child)
        return None

    def create_user(self, user: Tutor | Child) -> None:
        if isinstance(user, Tutor):
            tutor_entity = LoginTutorMapper.to_entity(user)
            self._tutot_repository.add(tutor_entity)
        elif isinstance(user, Child):
            child_entity = LoginChildMapper.to_entity(user)
            self._child_repository.add(child_entity)
        