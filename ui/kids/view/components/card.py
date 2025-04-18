import flet as ft

from domain.model import Routine, Exercise


class RoutineCard(ft.Card):
    """
    Clase base para representar una tarjeta de rutina.
    Esta clase hereda de `ft.Card` y se utiliza para mostrar información sobre una rutina. Es heredada en otras RoutineCard más especíalizadas.
    """
    
    def __init__(self, routine: Routine) -> None:
        super().__init__()
        self._routine = routine
    
    @property
    def routine(self) -> Routine:
        return self._routine

    @routine.setter
    def routine(self, routine: Routine) -> None:
        self._routine = routine


class HorizontalRoutineCard(RoutineCard):
    """
    Es un componente que representa una tarjeta de rutina en un diseño horizontal.
    Esta tarjeta muestra el nombre y la descripción de la rutina, así como botones para ver los ejercicios y agregar la rutina a favoritos.
    """

    def __init__(self, routine: Routine, on_favorite_button_click=None, on_show_exercises_button_click=None) -> None:
        super().__init__(routine)
        self.content = ft.ListTile(
            title=ft.Text(routine.name.capitalize()),
            subtitle=ft.Column(
                controls=[
                    ft.Text(routine.description.capitalize()),
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                text="Ver Ejercicios",
                                icon=ft.Icons.FITNESS_CENTER,
                                on_click=on_show_exercises_button_click,
                                data=routine
                            ),
                            ft.TextButton(
                                text="Agregar a favoritos",
                                icon=ft.Icons.FAVORITE_BORDER,
                                on_click=on_favorite_button_click,
                            ),
                        ]
                    ),
                ]
            )
        )


class ExerciseCard(ft.Card):
    """
    Clase base para representar una tarjeta de ejercicio.
    Esta clase hereda de `ft.Card` y se utiliza para mostrar información sobre un ejercicio. Es heredada en otras ExerciseCard más específicas.
    """
    
    def __init__(self, exercise: Exercise) -> None:
        self._exercise = exercise
        super().__init__(
            content=ft.ListTile(
                title=ft.Text(exercise.name.capitalize()),
                subtitle=ft.Text(exercise.description.capitalize()),
                leading=ft.Icon(ft.Icons.FITNESS_CENTER),
            )
        )
    
    @property
    def exercise(self) -> Exercise:
        return self._exercise

    @exercise.setter
    def exercise(self, exercise: Exercise) -> None:
        self._exercise = exercise
