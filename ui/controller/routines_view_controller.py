import flet as ft

from ui.view import RoutinesView
from ui.event import RoutinesViewEventsConnector
from hexagon.application.service import RoutinesServicePort


class RoutinesViewController:
    """
    Este controlador es responsable de manejar la lógica de presentación para la vista de rutinas. Interactúa con el puerto de servicio de rutinas ``(RoutinesServicePort)`` y la vista de rutinas ``(RoutinesView)``.
    Se encarga de inicializar la vista con todas las rutinas disponibles y conectar los eventos de la vista con el servicio de rutinas.

    Sólo devuelve la vista de rutinas y no tiene acceso a la lógica de negocio.
    """

    def __init__(self, routines_service_port: RoutinesServicePort, routines_view: RoutinesView) -> None:
        self._routines_view = routines_view
        self._events_connector = RoutinesViewEventsConnector(routines_service_port, routines_view)
        self._routines_view.routines = routines_service_port.get_all_routines()

    @property
    def view(self) -> ft.View:
        """
        Devuelve la vista de rutinas.
        """
        return self._routines_view
