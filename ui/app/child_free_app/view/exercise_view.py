import flet as ft

class ExerciseView(ft.View):
    def __init__(self):
        ejercicios = [
            {"id": 1, "nombre": "Saltos estrella", "descripcion": "Saltos abriendo brazos y piernas", "nivel": 1, "categoria": "Resistencia"},
            {"id": 2, "nombre": "Sentadillas básicas", "descripcion": "Sentadillas para principiantes", "nivel": 1, "categoria": "Fuerza"},
            {"id": 3, "nombre": "Estiramiento de brazos", "descripcion": "Estirar brazos en diferentes direcciones", "nivel": 1, "categoria": "Elasticidad"},
        ]
        super().__init__(
            route="/ejercicios",
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Ejercicios disponibles", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                        ft.Column([
                            ft.Container(
                                content=ft.Row([
                                    ft.Column([
                                        ft.Text(e["nombre"], weight=ft.FontWeight.BOLD, size=18),
                                        ft.Text(e["descripcion"], color="grey600", size=14),
                                        ft.Row([
                                            ft.Container(
                                                content=ft.Text(f"Nivel {e['nivel']}", size=12, color="green800", weight=ft.FontWeight.BOLD),
                                                bgcolor="green100", border_radius=8, padding=5, margin=ft.margin.only(right=5)
                                            ),
                                            ft.Container(
                                                content=ft.Text(e["categoria"], size=12, color="blue800", weight=ft.FontWeight.BOLD),
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
                            for e in ejercicios
                        ])
                    ])
                )
            ]
        )
