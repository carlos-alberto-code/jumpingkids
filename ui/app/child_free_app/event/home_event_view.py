import flet as ft

from domain.manager.service import Service
from domain.manager.view_event import ViewEvent

from ui.config.child_free_app import view_manager
from ui.app.child_free_app.view.home_view import HomeView


class HomeEventView:

    def __init__(self, home_view: HomeView) -> None:
        self._home_view = home_view
        self._connect_home_events()

    def on_exercise_section_click(self, event: ft.ControlEvent) -> None:
        module = "exercise"
        exercise_view = view_manager[module]
        event.page.views.clear()
        event.page.views.append(exercise_view)
        event.page.go(f"/{module}")
        event.page.update()
    
    def on_challenges_section_click(self, event: ft.ControlEvent) -> None:
        module = "desafios"
        challenges_view = view_manager[module]
        event.page.views.clear()
        event.page.views.append(challenges_view)
        event.page.go(f"/{module}")
        event.page.update()
    
    def on_personaje_section_click(self, event: ft.ControlEvent) -> None:
        module = "personajes"
        personaje_view = view_manager[module]
        event.page.views.clear()
        event.page.views.append(personaje_view)
        event.page.go(f"/{module}")
        event.page.update()
    
    def _connect_home_events(self) -> None:
        self._home_view.on_exercise_section_click = self.on_exercise_section_click
        self._home_view.on_challenges_section_click = self.on_challenges_section_click
        self._home_view.on_personaje_section_click = self.on_personaje_section_click
    

