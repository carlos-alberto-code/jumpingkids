from flet import View

from abc import ABC, abstractmethod


class Controller(ABC):
    """
    Clase abstracta que define la estructura de un controlador.
    """

    @property
    @abstractmethod
    def view(self) -> View:
        """
        Devuelve la vista asociada al controlador.
        """
        pass



    