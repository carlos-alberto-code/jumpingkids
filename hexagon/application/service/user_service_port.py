from abc import ABC, abstractmethod

from hexagon.domain.model import Routine


class UserServicePort(ABC):
    """
    Este es el servicio principal. Une otros puertos de repositorio para proporcionar las rutinas, y las rutinas favoritas de un usuario.
    """

    @abstractmethod
    def get_all_routines(self) -> list[Routine]:
        """
        Obtiene todas las rutinas disponibles, sin importar el usuario.
        """
        pass

    @abstractmethod
    def get_favorite_routines(self, user_id: int) -> list[Routine]:
        """
        Obtiene todas las rutinas favoritas de un usuario específico.
        """
        pass