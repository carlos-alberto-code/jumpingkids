import flet as ft

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from domain.manager.service import Service


T = TypeVar('T', bound=ft.View)


class ViewEvent(Generic[T], ABC):

    def __init__(self, view: T, services: list[Service]) -> None:
        super().__init__()
        self._view = view
        self._services = services
        self._connect_events()
    
    @property
    def view(self) -> T:
        """
        Devuelve la vista con sus eventos ya conectados. Los eventos hacen uso de servicios para suministrar datos para las acciones demandadas.
        """
        return self._view

    @abstractmethod
    def _connect_events(self) -> None:
        """
        Conecta los eventos de la vista con los servicios.
        """
        pass