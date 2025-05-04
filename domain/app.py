import flet as ft


class App:
    def __init__(self, theme: ft.Theme, views: list[ft.View]) -> None:
        self._theme = theme
        self._views = views
    
    @property
    def theme(self) -> ft.Theme:
        return self._theme
    
    @property
    def views(self) -> list[ft.View]:
        return self._views

