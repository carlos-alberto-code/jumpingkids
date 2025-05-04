import flet as ft


class App:
    def __init__(self, theme: ft.Theme, views: dict[str, ft.View]) -> None:
        self._theme = theme
        self._views = views
    
    @property
    def theme(self) -> ft.Theme:
        return self._theme
    
    @property
    def views(self) -> dict[str, ft.View]:
        return self._views

