from ui.view.components.sidebar.icon_text import IconText
from ui.view.components.sidebar.selectable import SelectableControl


class SidebarItem(SelectableControl):
    def __init__(self, label: str, icon: str, selected: bool = False, on_click=None) -> None:
        self._icon_text_control = IconText(label, icon)
        super().__init__(
            content=self._icon_text_control,
            selected=selected,
            on_click=on_click
        )
    
    @property
    def label(self) -> str:
        return self._icon_text_control.label
    
    @label.setter
    def label(self, label: str) -> None:
        self._icon_text_control.label = label
        self._icon_text_control.update()
    
    @property
    def icon(self) -> str:
        return self._icon_text_control.icon
    
    @icon.setter
    def icon(self, icon: str) -> None:
        self._icon_text_control.icon = icon
        self._icon_text_control.update()