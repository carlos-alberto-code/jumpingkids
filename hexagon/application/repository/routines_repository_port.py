from abc import ABC, abstractmethod
from hexagon.domain.model import Routine, Exercise


class RoutinesRepositoryPort(ABC):
    
    @abstractmethod
    def get_all_routines(self) -> list[Routine]:
        """
        Obtiene todas las rutinas disponibles.
        """
        pass

    @abstractmethod
    def get_exercises_by_routine_id(self, routine_id: int) -> list[Exercise] | None:
        """
        Obtiene todos los ejercicios de una rutina específica.
        """
        pass

    @abstractmethod
    def get_favorite_routines_by_user_id(self, user_id: int) -> list[Routine]:
        """
        Obtiene todas las rutinas favoritas de un usuario específico.
        """
        pass
    