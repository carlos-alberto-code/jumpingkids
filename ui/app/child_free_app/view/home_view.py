import flet as ft

from ui.app.child_free_app.components.challenge_card import PremiumBanner
from ui.app.child_free_app.components.home_view import (
    WelcomeComponent,
    StatsComponent,
    SectionsComponent,
    DailyTipComponent
)

from domain.model import Tutor, Child

class HomeView(ft.View):

    def __init__(self):

        self._user: Tutor | Child | None = None

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
    
    @property
    def user(self) -> Tutor | Child | None:
        return self._user
    
    @user.setter
    def user(self, value: Tutor | Child) -> None:
        self._user = value

    def _on_section_click(self, route):
        if self.page:
            self.page.go(route)