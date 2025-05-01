import flet as ft
from ui.app.child_free_app.components.home_view import (
    WelcomeComponent,
    StatsComponent,
    SectionsComponent,
    DailyTipComponent
)
from ui.app.child_free_app.components.challenge_card import PremiumBanner

class HomeView(ft.View):
    def __init__(self):
        # Crear instancias de los componentes refactorizados
        welcome_component = WelcomeComponent(username="Alberto")
        stats_component = StatsComponent()
        sections_component = SectionsComponent(on_section_click=self._on_section_click)
        daily_tip_component = DailyTipComponent()

        super().__init__(
            route="/home",
            appbar=None,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.ListView(
                        [
                            welcome_component,
                            stats_component,
                            sections_component,
                            daily_tip_component,
                            PremiumBanner()
                        ],
                        spacing=15,
                        padding=20,
                    )
                )
            ],
            bgcolor="#F3E5F5",  # Color de fondo lila claro como en ChildFreeTheme
        )

    def _on_section_click(self, route):
        if self.page:
            self.page.go(route)