"""
Este será un puerto de servicio para la autenticación de usuario. Debe determinar si el usuario existe, si la contraseña es correcta, y qué tipo de usuario es para determinar las capacidades de la aplicación.
"""

from abc import ABC, abstractmethod


class UserAuthServicePort(ABC):
    """
    Este es el puerto de servicio para la autenticación de usuario.
    """

    @abstractmethod
    def user_exists(self, username: str, password: str) -> bool:
        """
        Verifica si el usuario existe y si la contraseña es correcta.
        """
        pass

    @abstractmethod
    def get_user_type(self, username: str) -> str:
        """
        Obtiene el tipo de usuario (por ejemplo, niño, tutor, nutricionista).
        """
        pass
    