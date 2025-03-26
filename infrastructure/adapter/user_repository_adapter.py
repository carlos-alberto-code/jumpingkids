from hexagon.application.repository import UserRepositoryPort
from hexagon.domain.model import Routine


class UserRepositoryAdapter(UserRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
    
    def get_favorite_routines(self, user_id: int) -> list[Routine]:
        ...
    
    