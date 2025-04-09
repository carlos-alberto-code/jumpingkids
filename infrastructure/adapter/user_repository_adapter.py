from domain.model.model import Routine
from domain.application.repository import UserRepositoryPort


class UserRepositoryAdapter(UserRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
    
    def get_favorite_routines(self, user_id: int) -> list[Routine]:
        ...
    
    