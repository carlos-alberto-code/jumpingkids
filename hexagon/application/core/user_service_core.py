from hexagon.application.service import UserServicePort
from hexagon.application.repository import UserRepositoryPort
from hexagon.application.repository import RoutinesRepositoryPort
from hexagon.domain.model import Routine


class UserServiceCore(UserServicePort):

    def __init__(self, user_repository: UserRepositoryPort, routines_repository: RoutinesRepositoryPort) -> None:
        super().__init__()
        self._user_repository_port = user_repository
        self._routines_repository_port = routines_repository
    
    def get_all_routines(self) -> list[Routine]:
        routines: list[Routine] = self._routines_repository_port.get_all_routines()
        return routines

    def get_favorite_routines(self, user_id: int) -> list[Routine]:
        routines: list[Routine] = self._user_repository_port.get_favorite_routines(user_id)
        return routines