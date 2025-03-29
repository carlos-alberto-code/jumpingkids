import flet as ft


class SelectableControl(ft.Container):
    def __init__(
        self, 
        content=None, 
        selected: bool = False, 
        on_click=None, 
        highlight_color=ft.Colors.AMBER,
        default_text_color=ft.Colors.WHITE,
    ) -> None:
        self._selected = selected
        self._on_click_event = on_click
        self._highlight_color = highlight_color
        self._default_text_color = default_text_color
        
        super().__init__(
            content=content,
            padding=ft.padding.symmetric(horizontal=10, vertical=5),
            on_click=self._on_click_event,
            ink=True,
            on_hover=self._on_hover,
            bgcolor=ft.Colors.BLUE_GREY_800 if selected else None,
            border_radius=10,
        )
    
    def _on_hover(self, e: ft.ControlEvent):
        self.bgcolor = ft.Colors.BLUE_GREY_700 if e.data == "true" else (ft.Colors.BLUE_GREY_800 if self._selected else None)
        self.update()
    
    @property
    def selected(self) -> bool:
        return self._selected
    
    @selected.setter
    def selected(self, selected: bool) -> None:
        self._selected = selected
        self.bgcolor = self._highlight_color if selected else self._default_text_color
        self.update()