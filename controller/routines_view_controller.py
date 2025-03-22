import flet as ft

from view import RoutinesView
from event import RoutinesViewEvents
from hexagon.domain.model import Routine
from hexagon.application.service import RoutinesServicePort



class RoutinesViewController:

    def __init__(self, routines_service_port: RoutinesServicePort, routines_view: RoutinesView) -> None:
        self._routines_view = routines_view
        self._routines_service_port = routines_service_port
        self._events = RoutinesViewEvents(routines_service_port)
        self._connect_events_with_view()
        self._routines_view.routines = self._routines_service_port.get_all_routines()

    @property
    def view(self) -> ft.View:
        """
        Devuelve la vista de rutinas.
        """
        return self._routines_view
    
    def _connect_events_with_view(self) -> None:
        """
        Conecta los eventos de la vista con los métodos del controlador.
        """
        self._routines_view.on_view_exercises_button_click = self._events.on_view_exercises_button_click
        self._routines_view.on_favorite_button_click = self._events.on_favorite_button_click
        self._routines_view.on_filter_by_favorite_button_click = self._events.on_filter_by_favorite_button_click
        self._routines_view.on_filter_by_category_button_click = self._events.on_filter_by_category_button_click