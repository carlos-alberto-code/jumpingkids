import flet as ft

class ExerciseCard(ft.Container):
    def __init__(self, nombre, descripcion, nivel, categoria):
        super().__init__(
            content=ft.Row([
                ft.Column([
                    ft.Text(nombre, weight=ft.FontWeight.BOLD, size=18),
                    ft.Text(descripcion, color="grey600", size=14),
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"Nivel {nivel}", size=12, color="green800", weight=ft.FontWeight.BOLD),
                            bgcolor="green100", border_radius=8, padding=5, margin=ft.margin.only(right=5)
                        ),
                        ft.Container(
                            content=ft.Text(categoria, size=12, color="blue800", weight=ft.FontWeight.BOLD),
                            bgcolor="blue100", border_radius=8, padding=5
                        ),
                    ], spacing=5)
                ]),
                ft.Container(
                    content=ft.Icon(ft.icons.PLAY_CIRCLE_FILL, color="white", size=32),
                    bgcolor="green500", border_radius=50, padding=8
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor="white", border_radius=16, padding=16, margin=ft.margin.only(bottom=10), border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100")
        )
