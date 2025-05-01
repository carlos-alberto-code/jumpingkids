import flet as ft
from ui.app.child_free_app.components.exercise_card import ExerciseCard

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
                            ExerciseCard(
                                nombre=e["nombre"],
                                descripcion=e["descripcion"],
                                nivel=e["nivel"],
                                categoria=e["categoria"]
                            ) for e in ejercicios
                        ])
                    ])
                )
            ]
        )
