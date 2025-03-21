import flet as ft

from view import RoutinesView
from domain.model import Exercise, Routine
from application.core import RoutinesServiceCore
from application.service import RoutinesServicePort


class RoutinesViewController:

    def __init__(self):
        self._routines_service_port: RoutinesServicePort = RoutinesServiceCore()
        self._rotuines_view = RoutinesView(
            on_favorite_button_click=self.on_favorite_button_click,
            on_view_exercises_button_click=self.on_view_exercises_button_click,
            on_filter_by_favorite_button_click=self.on_filter_by_favorite_button_click,
            on_filter_by_category_button_click=self.on_filter_by_category_button_click,
        )

    def on_view_exercises_button_click(self, event: ft.ControlEvent):
        """
        Muestra los ejercicios de una rutina específica.
        """
        exercises: list[Exercise] = self._routines_service_port.get_exercises_by_routine_id(1)
        for exercise in exercises:
            print(f"Ejercicio: {exercise.name}, Descripción: {exercise.description}")
        # Conectar los ejercicios con la vista y actualizar la GUI

    def on_favorite_button_click(self, event: ft.ControlEvent):
        """
        Agrega o elimina la rutina a una lista de favoritos del usuario.
        """
        user_id = 1 # TODO: Hay que buscar una forma de obtener el id del usuario
        routine_id = 2 # TODO: Hay que buscar una forma de obtener el id de la rutina
        self._routines_service_port.add_routine_to_user_favorite_list(user_id, routine_id) # Se requiere el id del usuario y el id de la rutina para agregarla
        self._routines_service_port.remove_routine_from_user_favorite_list(user_id, routine_id) # Se requiere el id del usuario y el id de la rutina para eliminarla

        # Mostrar un mensaje de éxito o error

    def on_filter_by_favorite_button_click(self, event: ft.ControlEvent):
        """
        Filtra las rutinas favoritas del usuario.
        """
        user_id = 1 # TODO: Hay que buscar una forma de obtener el id del usuario
        favorite_routines: list[Routine] = self._routines_service_port.get_favorite_routines_by_user_id(user_id)
        for routine in favorite_routines:
            print(f"Rutina favorita: {routine.name}, Descripción: {routine.description}")
        # Conectar las rutinas obtenidas con la vista y actualizar la GUI

    def on_filter_by_category_button_click(self, event: ft.ControlEvent):
        """
        Filtra las rutinas en función de la categoría seleccionada.
        """
        category_id = 1 # TODO: Hay que buscar una forma de obtener el id de la categoría
        category_routines: list[Routine] = self._routines_service_port.get_routines_by_category_id(category_id)
        for routine in category_routines:
            print(f"Rutina por categoría: {routine.name}, Descripción: {routine.description}")
        # Conectar las rutinas obtenidas con la vista y actualizar la GUI
