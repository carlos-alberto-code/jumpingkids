import flet as ft
from ui.app.child_free_app.components.personaje_components import AvatarCard, AchievementSummary, PremiumBannerPersonaje

class PersonajeView(ft.View):
    def __init__(self):
        super().__init__(
            route="/personaje",
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Tu personaje", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                        AvatarCard(
                            nombre="Aventurero Inicial",
                            descripcion="¡Personaliza tu avatar y comienza tu aventura de ejercicios!"
                        ),
                        AchievementSummary(medallas=2, nivel=1),
                        ft.Container(
                            content=ft.Text("Personalizar avatar", color="white", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                            bgcolor="green500", border_radius=8, padding=ft.padding.symmetric(vertical=12), width=float("inf")
                        ),
                        PremiumBannerPersonaje()
                    ])
                )
            ]
        )
