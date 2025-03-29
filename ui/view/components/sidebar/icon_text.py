import flet as ft


class IconText(ft.Row):

    def __init__(self, label: str, icon: str) -> None:
        super().__init__(spacing=10,alignment=ft.MainAxisAlignment.START)
        self._label = label
        self._icon = icon
        self.controls = [ft.Icon(self._icon, color=ft.Colors.WHITE), ft.Text(self._label, color=ft.Colors.WHITE, size=16)]
    
    @property
    def label(self) -> str:
        return self._label
    
    @label.setter
    def label(self, label: str) -> None:
        self._label = label
        self.controls = [ft.Icon(self._icon), ft.Text(self._label)]
    
    @property
    def icon(self) -> str:
        return self._icon
    
    @icon.setter
    def icon(self, icon: str) -> None:
        self._icon = icon
        self.controls = [ft.Icon(self._icon), ft.Text(self._label)]
