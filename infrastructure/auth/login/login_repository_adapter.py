from domain.auth.login.login_repository_port import LoginRepositoryPort
from domain.model import Child, Tutor

from infrastructure.auth.login.login_mapper import LoginChildMapper, LoginTutorMapper
from infrastructure.repository import Repository
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
        