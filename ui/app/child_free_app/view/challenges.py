import flet as ft

class ChallengesView(ft.View):
    def __init__(self):
        desafios = [
            {"id": 1, "nombre": "Misión espacial", "descripcion": "Completa 5 ejercicios para viajar a la luna", "personaje": "Astronauta Alex", "dias": 5, "medalla": "bronce"},
            {"id": 2, "nombre": "Aventura en la selva", "descripcion": "Supera obstáculos como un explorador", "personaje": "Exploradora Mia", "dias": 7, "medalla": "bronce"},
        ]
        super().__init__(
            route="/desafios",
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Desafíos disponibles", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                        ft.Column([
                            ft.Container(
                                content=ft.Row([
                                    ft.Container(
                                        content=ft.Icon(ft.icons.STAR, color="#FFB800", size=28),
                                        bgcolor="yellow100", border_radius=50, padding=8, margin=ft.margin.only(right=10)
                                    ),
                                    ft.Column([
                                        ft.Text(d["nombre"], weight=ft.FontWeight.BOLD, size=18),
                                        ft.Text(d["descripcion"], color="grey600", size=14),
                                        ft.Row([
                                            ft.Icon(ft.icons.PERSON, color="blue500", size=16),
                                            ft.Text(d["personaje"], size=14, color="blue500")
                                        ], spacing=5),
                                        ft.Row([
                                            ft.Container(
                                                content=ft.Text(f"{d['dias']} días", size=12, color="orange800", weight=ft.FontWeight.BOLD),
                                                bgcolor="orange100", border_radius=8, padding=5
                                            ),
                                            ft.Row([
                                                ft.Icon(ft.icons.MILITARY_TECH, color="amber600", size=16),
                                                ft.Text(f"Medalla de {d['medalla']}", size=12, color="amber600")
                                            ], spacing=3)
                                        ], alignment=ft.MainAxisAlignment.START)
                                    ], expand=True)
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                bgcolor="white", border_radius=16, padding=16, margin=ft.margin.only(bottom=10), border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100")
                            )
                            for d in desafios
                        ]),
                        ft.Container(
                            margin=ft.margin.only(top=10),
                            bgcolor="green50", border_radius=12, padding=12,
                            content=ft.Row([
                                ft.Container(
                                    content=ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_UP, color="green600", size=20),
                                    bgcolor="green100", border_radius=50, padding=8, margin=ft.margin.only(right=10)
                                ),
                                ft.Text("¡Obtén más desafíos con el plan premium!", color="green800", size=14, weight=ft.FontWeight.W_100),
                                ft.Container(
                                    content=ft.Text("Actualizar", color="white", size=12, weight=ft.FontWeight.W_100),
                                    bgcolor="green500", border_radius=50, padding=ft.padding.symmetric(horizontal=12, vertical=6)
                                )
                            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                        )
                    ])
                )
            ]
        )
