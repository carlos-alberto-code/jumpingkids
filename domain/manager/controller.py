import flet as ft

from domain.manager.event import ViewEvent
from domain.manager.service import Service
from domain.manager.repository import Repository


class Controller:
    """
    El controlador es el encargado de hacer match entre todos los insumos necesarios para crear una vista; dar vida a una pantalla. Este marco requiere de un controlador para cada vista. El controlador a su vez requiere de una clase que representa la vista, una clase que representa la lógica de eventos de la vista y una lista de clases que representan los servicios que se utilizarán en la vista. Cada servicio requiere de una lista de clases que representan los repositorios que se utilizarán en el servicio.

    El controlador hace match entre todos estos componentes y los conecta entre sí, para finalmente devolver la vista con sus eventos ya conectados, de forma que pueda existir persistencia de datos basado en eventos.
    """

    def __init__(
        self,
        view_class: type[ft.View],
        event_class: type[ViewEvent],
        service_classes: dict[type[Service], list[type[Repository]]]
    ) -> None:
        self._view_class = view_class
        self._event_class = event_class
        self._services_class = service_classes
    
    def build(self) -> ft.View:
        """
        Devuelve la vista con sus eventos ya conectados. Los eventos hacen uso de servicios para suministrar datos para las acciones demandadas.
        """
        view = self._view_class()
        services_dict = {}
        for service_class, repositories in self._services_class.items():
            service_instance = service_class(
                *[repository() for repository in repositories]
            )
            services_dict[service_class] = service_instance
        return self._event_class(view, services_dict).view
    