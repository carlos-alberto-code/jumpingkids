import flet as ft

from ui.view import RoutinesView
from hexagon.domain.model import Exercise, Routine
from hexagon.application.service import RoutinesServicePort, UserServicePort


class RoutinesViewEventsConnector:
    """
    La clase empareja la definicón de los eventos con la vista. Hace uso de un servicio para manejar la lógica de negocio y conectar los resultados con la parte gráfica. Esta clase tiene todos los eventos que se pueden disparar desde la vista de rutinas y genera esa conexión internamente.
    """

    def __init__(
            self,
            routines_view: RoutinesView,
            user_service_port: UserServicePort,
            routines_service_port: RoutinesServicePort,
    ) -> None:
        self._routines_view = routines_view
        self._user_service_port = user_service_port
        self._routines_service_port = routines_service_port
        self._connect_events()

    def _on_view_exercises_button_click(self, event: ft.ControlEvent):
        """
        Muestra los ejercicios de una rutina específica.
        """
        exercises: list[Exercise] = self._routines_service_port.get_exercises_by_routine_id(
            1)
        print(exercises)
        # Conectar los ejercicios con la vista y actualizar la GUI

    def _on_favorite_button_click(self, event: ft.ControlEvent):
        """
        Agrega o elimina la rutina a una lista de favoritos del usuario.
        """
        control: ft.TextButton = event.control
        print(control)
        # user_id = 1  # TODO: Hay que buscar una forma de obtener el id del usuario
        # routine_id = 2  # TODO: Hay que buscar una forma de obtener el id de la rutina
        # # Se requiere el id del usuario y el id de la rutina para agregarla
        # self._routines_service_port.add_routine_to_user_favorite_list(
        #     user_id, routine_id)
        # # Se requiere el id del usuario y el id de la rutina para eliminarla
        # self._routines_service_port.remove_routine_from_user_favorite_list(
        #     user_id, routine_id)

        # Mostrar un mensaje de éxito o error

    def _on_filter_by_favorite_button_click(self, event: ft.ControlEvent):
        """
        Filtra las rutinas favoritas del usuario.
        """
        user_id = 1  # TODO: Hay que buscar una forma de obtener el id del usuario
        # favorite_routines: list[Routine] = self._routines_service_port.get_favorite_routines_by_user_id(
        #     user_id)
        # for routine in favorite_routines:
        #     print(
        #         f"Rutina favorita: {routine.name}, Descripción: {routine.description}")
        # Conectar las rutinas obtenidas con la vista y actualizar la GUI

    def _on_filter_by_category_button_click(self, event: ft.ControlEvent):
        """
        Filtra las rutinas en función de la categoría seleccionada.
        """
        category_id = 1  # TODO: Hay que buscar una forma de obtener el id de la categoría
        # category_routines: list[Routine] = self._routines_service_port.get_routines_by_category_id(
        #     category_id)
        # for routine in category_routines:
        #     print(
        #         f"Rutina por categoría: {routine.name}, Descripción: {routine.description}")
        # Conectar las rutinas obtenidas con la vista y actualizar la GUI

    def _connect_events(self) -> None:
        """
        Conecta los eventos de la vista con los métodos del controlador.
        """
        self._routines_view.on_view_exercises_button_click = self._on_view_exercises_button_click
        self._routines_view.on_favorite_button_click = self._on_favorite_button_click
        self._routines_view.on_filter_by_favorite_button_click = self._on_filter_by_favorite_button_click
        self._routines_view.on_filter_by_category_button_click = self._on_filter_by_category_button_click
