import flet as ft


class JView:
    def __init__(self, name: str, icon: ft.Icons, view: ft.View) -> None:
        self._name = name
        self._icon = icon
        self._view = view
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def icon(self) -> ft.Icons:
        return self._icon
    
    @property
    def view(self) -> ft.View:
        return self._view


class App:
    def __init__(self, theme: ft.Theme, views: dict[str, JView]) -> None:
        self._theme = theme
        self._views = views
    
    @property
    def theme(self) -> ft.Theme:
        return self._theme
    
    @property
    def views(self) -> dict[str, JView]:
        return self._views

