import flet as ft

from hexagon.domain.model import Routine


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

    def __init__(self, routine: Routine, on_favorite_button_click=None, on_card_click=None) -> None:
        super().__init__(routine)
        self.content = ft.ListTile(
            leading=ft.Image(
                src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3Q3ZDEwYWRleWwwZm50bWtsOGF0bDF0Z282YTNnZmdsYmttZ2Z6ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OLY40BwPRUWic/giphy.gif",

            ),
            title=ft.Text(routine.name),
            subtitle=ft.Column(
                controls=[
                    ft.Text(routine.description),
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                text="Ver Ejercicios",
                                icon=ft.Icons.FITNESS_CENTER,
                                on_click=on_card_click,
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
