import flet as ft

from hexagon.domain.model import Routine
from ui.view.components.card import ExerciseCard, HorizontalRoutineCard


class RoutinesViewLayout(ft.Column):
    """
    Esta clase representa el diseño de la vista de rutinas en general. Recibe todos los eventos definidos y suministra las referencias a cada componente.
    """

    def __init__(
            self,
            routines: list[Routine],
            on_favorite_button_click=None,
            on_show_exercises_button_click=None,
            on_submit=None,
            on_filter_by_category_button_click=None,
            on_filter_by_favorites_button_click=None,
    ) -> None:
        super().__init__(expand=True)
        self._routines = routines
        self.controls = [
            ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            self._create_search_row(
                                on_submit=on_submit,
                                on_filter_by_category_button_click=on_filter_by_category_button_click,
                                on_filter_by_favorites_button_click=on_filter_by_favorites_button_click,
                            ),
                            self._create_routines_list(
                                routine_cards=[
                                    HorizontalRoutineCard(
                                        routine=routine,
                                        on_favorite_button_click=on_favorite_button_click,
                                        on_show_exercises_button_click=on_show_exercises_button_click,
                                    ) for routine in routines
                                ]
                            )
                        ],
                        expand=True,
                    ),
                    ft.Column(width=400),
                ],
                expand=True,
            )
        ]

    def _create_search_row(self, on_submit=None, on_filter_by_category_button_click=None, on_filter_by_favorites_button_click=None) -> ft.Row:
        return ft.Row(
            controls=[
                ft.TextField(
                    label="Buscar rutina",
                    prefix_icon=ft.Icons.SEARCH,
                    border_radius=10,
                    text_size=12,
                    label_style=ft.TextStyle(size=12),
                    height=40,
                    expand=True,
                    on_submit=on_submit,
                ),
                ft.PopupMenuButton(
                    icon=ft.Icons.FILTER_LIST,
                    items=[
                        ft.PopupMenuItem(
                            text="Filtrar por categoría",
                            icon=ft.Icons.FILTER_LIST,
                            on_click=on_filter_by_category_button_click,
                        ),
                        ft.PopupMenuItem(
                            text="Filtrar por favoritos",
                            icon=ft.Icons.FAVORITE,
                            on_click=on_filter_by_favorites_button_click,
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.END,
        )
    
    def _create_routines_list(self, routine_cards: list[HorizontalRoutineCard]) -> ft.ListView:
        return ft.ListView(
            controls=routine_cards,
            expand=True,
        )
    
    def _create_exercise_list(self, exercises: list[ExerciseCard]) -> ft.ListView:
        return ft.ListView(
            controls=exercises,
            expand=True,
        )
