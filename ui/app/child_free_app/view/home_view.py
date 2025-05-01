import flet as ft

from ui.app.child_free_app.components.section import SectionHome


class HomeView(ft.View):

    def __init__(self):
        super().__init__(
            route="/home",
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("¡Bienvenido!", size=26, weight=ft.FontWeight.BOLD, color="green700"),
                        ft.Text("Explora y diviértete con tus actividades", size=16, color="grey600", weight=ft.FontWeight.W_400, text_align=ft.TextAlign.LEFT),
                        ft.Column([
                            ft.Container(
                                bgcolor="white", border_radius=16, padding=16, border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100"), margin=ft.margin.only(bottom=16),
                                content=ft.Row([
                                    ft.Container(
                                        content=ft.Icon(ft.icons.FITNESS_CENTER, color="green500", size=40),
                                        bgcolor="green50", border_radius=50, padding=12, margin=ft.margin.only(right=16)
                                    ),
                                    ft.Column([
                                        ft.Text("Ejercicios", weight=ft.FontWeight.BOLD, size=18, color="green800"),
                                        ft.Text("¡Actívate con ejercicios divertidos!", color="grey600", size=14),
                                        ft.Container(
                                            content=ft.Text("Ver ejercicios", color="white", size=12, weight=ft.FontWeight.W_100),
                                            bgcolor="green500", border_radius=50, padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                            on_click=lambda e: print("Click en Ejercicios")
                                        )
                                    ], expand=True)
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ),
                            ft.Container(
                                bgcolor="white", border_radius=16, padding=16, border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100"), margin=ft.margin.only(bottom=16),
                                content=ft.Row([
                                    ft.Container(
                                        content=ft.Icon(ft.icons.STAR, color="#FFB800", size=40),
                                        bgcolor="yellow100", border_radius=50, padding=12, margin=ft.margin.only(right=16)
                                    ),
                                    ft.Column([
                                        ft.Text("Desafíos", weight=ft.FontWeight.BOLD, size=18, color="green800"),
                                        ft.Text("Supera retos y gana medallas", color="grey600", size=14),
                                        ft.Container(
                                            content=ft.Text("Ver desafíos", color="white", size=12, weight=ft.FontWeight.W_100),
                                            bgcolor="green500", border_radius=50, padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                            on_click=lambda e: print("Click en Desafíos")
                                        )
                                    ], expand=True)
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            ),
                            ft.Container(
                                bgcolor="white", border_radius=16, padding=16, border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100"),
                                content=ft.Row([
                                    ft.Container(
                                        content=ft.Icon(ft.icons.PERSON, color="blue500", size=40),
                                        bgcolor="blue50", border_radius=50, padding=12, margin=ft.margin.only(right=16)
                                    ),
                                    ft.Column([
                                        ft.Text("Personajes", weight=ft.FontWeight.BOLD, size=18, color="green800"),
                                        ft.Text("Personaliza tu avatar y mira tus logros", color="grey600", size=14),
                                        ft.Container(
                                            content=ft.Text("Ver personaje", color="white", size=12, weight=ft.FontWeight.W_100),
                                            bgcolor="green500", border_radius=50, padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                            on_click=lambda e: print("Click en Personajes")
                                        )
                                    ], expand=True)
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            )
                        ])
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                )
            ]
        )
