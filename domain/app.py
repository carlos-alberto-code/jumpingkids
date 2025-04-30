import flet as ft


class JumpingkidsTheme(ft.Theme):
    pass


class App:
    def __init__(self, theme: JumpingkidsTheme, content: ft.Control) -> None:
        self._theme = theme
        self._content = content
    
    @property
    def theme(self) -> JumpingkidsTheme:
        return self._theme
    
    @property
    def content(self) -> ft.Control:
        return self._content


class TutorFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme, content: ft.Control) -> None:
        super().__init__(theme, content)
        


class TutorPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme, content: ft.Control) -> None:
        super().__init__(theme, content)



class ChildFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme, content: ft.Control) -> None:
        super().__init__(theme, content)


class ChildPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme, content: ft.Control) -> None:
        super().__init__(theme, content)
