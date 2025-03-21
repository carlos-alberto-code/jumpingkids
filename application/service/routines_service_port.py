from abc import ABC, abstractmethod

from domain.model import Exercise, Routine


class RoutinesServicePort(ABC):
    """
    Este servicio une los repositorios de rutinas, ejercicios y usuarios para proporcionar unicamente las rutinas relacionadas con un usuario, así como relacionar rutinas con usuarios para marcarlas como favoritas.
    """

    @abstractmethod
    def get_all_routines(self) -> list[Routine]:
        """
        Obtiene todas las rutinas disponibles.
        """
        pass

    @abstractmethod
    def get_exercises_by_routine_id(self, routine_id: int) -> list[Exercise]:
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

    @abstractmethod
    def get_routines_by_category_id(self, category_id: int) -> list[Routine]:
        """
        Obtiene todas las rutinas de una categoría específica.
        """
        pass

    @abstractmethod
    def add_routine_to_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        """
        Agrega una rutina a la lista de favoritos de un usuario.
        """
        pass

    @abstractmethod
    def remove_routine_from_user_favorite_list(self, user_id: int, routine_id: int) -> None:
        """
        Elimina una rutina de la lista de favoritos de un usuario.
        """
        pass
