import flet as ft

from hexagon.domain.model import Routine
from ui.view.components.routine_card import HorizontalRoutineCard


class RoutinesViewLayout(ft.Container):

    def __init__(self, routines: list[Routine]) -> None:
        super().__init__()
        self.content = ft.Column(
            controls=[
                self._create_search_row(),
                self._create_routines_list(
                    routine_cards=[
                        HorizontalRoutineCard(
                            routine=routine,
                            on_favorite_button_click=lambda e: print(f"Favoritar rutina {routine.name}"),
                            on_card_click=lambda e: print(f"Ver ejercicios de la rutina {routine.name}"),
                        ) for routine in routines
                    ]
                )
            ]
        )

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
            spacing=10,
            build_controls_on_demand=True,
        )
