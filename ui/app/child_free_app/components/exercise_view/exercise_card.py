import flet as ft
from domain.model import Exercise

class ExerciseCard(ft.Card):
    def __init__(
        self, 
        exercise: Exercise,
        on_click= None
    ):
        super().__init__(
            content=ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(exercise.name, weight=ft.FontWeight.BOLD, size=18),
                        ft.Text(exercise.description, color="grey600", size=14),
                        ft.Row([
                            ft.Container(
                                content=ft.Text(f"Nivel {exercise.level}", size=12, color="green800", weight=ft.FontWeight.BOLD),
                                bgcolor="green100", border_radius=8, padding=5, margin=ft.margin.only(right=5)
                            ),
                            ft.Container(
                                content=ft.Text(exercise.category, size=12, color="blue800", weight=ft.FontWeight.BOLD),
                                bgcolor="blue100", border_radius=8, padding=5
                            ),
                        ], spacing=5)
                    ]),
                    ft.IconButton(
                        icon=ft.icons.PLAY_CIRCLE_FILL,
                        icon_color="white",
                        icon_size=32,
                        bgcolor="green500",
                        style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                            padding=8,
                        ),
                        on_click=on_click
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=16,
            ),
            elevation=4,
            margin=ft.margin.only(bottom=10),
            color=ft.colors.WHITE,
            surface_tint_color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=16),
        )
