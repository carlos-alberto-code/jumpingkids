import flet as ft
from domain.routing.controller import Controller

class Module:
    def __init__(self, name: str, icon: ft.Icons, route: str, controller: Controller) -> None:
        self._name = name
        self._icon = icon
        self._route = route
        self._controller = controller
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def icon(self) -> ft.Icons:
        return self._icon
    
    @property
    def route(self) -> str:
        return self._route
    
    @property
    def controller(self) -> Controller:
        return self._controller
