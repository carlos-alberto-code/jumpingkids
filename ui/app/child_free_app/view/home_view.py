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

    def __init__(
        self,
        on_exercise_section_click=None,
        on_challenges_section_click=None,
        on_personaje_section_click=None,
        user: Tutor | Child | None = None
    ) -> None:

        self._user: Tutor | Child | None = user

        # Eventos de clic en secciones
        self._on_exercise_section_click = on_exercise_section_click
        self._on_challenges_section_click = on_challenges_section_click
        self._on_personaje_section_click = on_personaje_section_click

        welcome_component = WelcomeComponent(username="Alberto")
        stats_component = StatsComponent()
        sections_component = SectionsComponent(
            on_exercise_click=self._on_exercise_section_click,
            on_challenges_click=self._on_challenges_section_click,
            on_personaje_click=self._on_personaje_section_click
        )
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
    
    @property
    def on_exercise_section_click(self):
        return self._on_exercise_section_click
    
    @on_exercise_section_click.setter
    def on_exercise_section_click(self, func):
        self._on_exercise_section_click = func

    @property
    def on_challenges_section_click(self):
        return self._on_challenges_section_click
    
    @on_challenges_section_click.setter
    def on_challenges_section_click(self, func):
        self._on_challenges_section_click = func

    @property
    def on_personaje_section_click(self):
        return self._on_personaje_section_click

    @on_personaje_section_click.setter
    def on_personaje_section_click(self, func):
        self._on_personaje_section_click = func
        