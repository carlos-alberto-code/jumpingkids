import flet as ft

from ui.kids.view.routines_view import RoutinesView
from ui.kids.controller.controller import Controller
from ui.kids.event.routines_view_event import RoutinesViewEventsConnector

from hexagon.application.service import UserServicePort, RoutinesServicePort


class RoutinesViewController(Controller):
    """
    Este controlador es responsable de manejar la lógica de presentación para la vista de rutinas. Interactúa con el puerto de servicio de rutinas ``(RoutinesServicePort)`` y la vista de rutinas ``(RoutinesView)``.
    Se encarga de inicializar la vista con todas las rutinas disponibles y conectar los eventos de la vista con el servicio de rutinas.

    Sólo devuelve la vista de rutinas y no tiene acceso a la lógica de negocio.
    """

    def __init__(
            self,
            routines_view: RoutinesView,
            user_service: UserServicePort,
            routines_service: RoutinesServicePort,
    ) -> None:
        self._routines_view = routines_view
        self._events_connector = RoutinesViewEventsConnector(
            routines_view=routines_view,
            user_service_port=user_service,
            routines_service_port=routines_service,
        )
        self._routines_view.routines = routines_service.get_all_routines()

    @property
    def view(self) -> ft.View:
        return self._routines_view
