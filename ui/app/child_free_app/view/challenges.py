import flet as ft
from ui.app.child_free_app.components.challenge_card import ChallengeCard, PremiumBanner

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
                            ChallengeCard(
                                nombre=d["nombre"],
                                descripcion=d["descripcion"],
                                personaje=d["personaje"],
                                dias=d["dias"],
                                medalla=d["medalla"]
                            ) for d in desafios
                        ]),
                        PremiumBanner()
                    ])
                )
            ]
        )
