import flet as ft
from ui.app.child_free_app.components.exercise_card import ExerciseCard
from domain.model import Exercise

class ExerciseView(ft.View):
    def __init__(self, appbar: ft.AppBar | None = None) -> None:
        ejercicios = [
            Exercise(id=1, name="Saltos estrella", description="Saltos abriendo brazos y piernas", level=1, category="Resistencia"),
            Exercise(id=2, name="Sentadillas básicas", description="Sentadillas para principiantes", level=1, category="Fuerza"),
            Exercise(id=3, name="Estiramiento de brazos", description="Estirar brazos en diferentes direcciones", level=1, category="Elasticidad"),
            Exercise(id=4, name="Flexiones de brazos", description="Flexiones para fortalecer el tren superior", level=2, category="Fuerza"),
            Exercise(id=5, name="Abdominales", description="Ejercicio para fortalecer el abdomen", level=2, category="Fuerza"),
            Exercise(id=6, name="Caminata rápida", description="Caminata a paso ligero para mejorar resistencia", level=1, category="Cardio"),
        ]
        super().__init__(
            route="/ejercicios",
            appbar=appbar,
            controls=[
                ft.Container(
                    padding=20,
                    expand=True,
                    content=ft.Row(
                        spacing=20,
                        controls=[
                            # Contenedor para la lista de ejercicios (50% del ancho)
                            ft.Container(
                                expand=2,
                                content=ft.Column([
                                    ft.Text("Ejercicios disponibles", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                                    ft.ListView([
                                        ExerciseCard(
                                            exercise=exercise,
                                        ) for exercise in ejercicios
                                    ], expand=True)
                                ], expand=True)
                            ),
                            
                            # Contenedor para la animación (50% del ancho)
                            ft.Container(
                                expand=2,
                                border_radius=16,
                                bgcolor="green50",
                                padding=16,
                                alignment=ft.alignment.center,
                                content=ft.Column([
                                    ft.Text("¡Ejercítate!", size=18, weight=ft.FontWeight.BOLD, color="green700"),
                                    ft.Container(
                                        expand=True,
                                        content=ft.Lottie(
                                            "https://app.lottiefiles.com/animation/951cb01d-90cc-40d2-aba5-980971103777",
                                            width=200,
                                            height=200,
                                            repeat=True,
                                            animate=True
                                        ),
                                        alignment=ft.alignment.center,
                                    )
                                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            )
                        ]
                    )
                )
            ]
        )
