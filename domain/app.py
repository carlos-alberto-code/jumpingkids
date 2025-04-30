import flet as ft

from domain.routing.view_manager import ViewManager


class JumpingkidsTheme(ft.Theme):
    pass


class App:
    def __init__(self, theme: JumpingkidsTheme, view_manager: ViewManager) -> None:
        self._theme = theme
        self._view_manager = view_manager
    
    @property
    def theme(self) -> JumpingkidsTheme:
        return self._theme
    
    @property
    def view_manager(self) -> ViewManager:
        return self._view_manager


class TutorFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme, view_manager: ViewManager) -> None:
        super().__init__(theme, view_manager)
        


class TutorPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme, view_manager: ViewManager) -> None:
        super().__init__(theme, view_manager)



class ChildFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme, view_manager: ViewManager) -> None:
        super().__init__(theme, view_manager)


class ChildPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme, view_manager: ViewManager) -> None:
        super().__init__(theme, view_manager)
