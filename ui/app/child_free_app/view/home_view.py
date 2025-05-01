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
                            SectionHome(
                                title="Ejercicios",
                                subtitle="¡Actívate con ejercicios divertidos!",
                                icon=ft.Icon(ft.icons.FITNESS_CENTER, color="green500", size=40),
                                icon_bgcolor="green50",
                                on_click=lambda e: print("Click en Ejercicios")
                            ),
                            SectionHome(
                                title="Desafíos",
                                subtitle="Supera retos y gana medallas",
                                icon=ft.Icon(ft.icons.STAR, color="#FFB800", size=40),
                                icon_bgcolor="yellow100",
                                on_click=lambda e: print("Click en Desafíos")
                            ),
                            SectionHome(
                                title="Personajes",
                                subtitle="Personaliza tu avatar y mira tus logros",
                                icon=ft.Icon(ft.icons.PERSON, color="blue500", size=40),
                                icon_bgcolor="blue50",
                                on_click=lambda e: print("Click en Personajes")
                            )
                        ])
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                )
            ]
        )
