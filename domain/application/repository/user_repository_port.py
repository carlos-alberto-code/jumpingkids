from abc import ABC, abstractmethod

from domain.model.model import Routine


class UserRepositoryPort(ABC):

    @abstractmethod
    def get_favorite_routines(self, user_id: int) -> list[Routine]:
        pass