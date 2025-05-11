import flet as ft

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from domain.manager.service import Service


V = TypeVar('V', bound=ft.View)
S = TypeVar('S', bound=Service)


class ViewEvent(Generic[V], ABC):

    def __init__(self, view: V, services: dict[type[Service], Service]) -> None:
        super().__init__()
        self._view = view
        self._services = services
        self._connect_events()
    
    @property
    def view(self) -> V:
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

    def get_service(self, service_class: type[S]) -> S:
        if service_class not in self._services:
            raise KeyError(f"El servicio {service_class.__name__} no está registrado.")
        return self._services[service_class]