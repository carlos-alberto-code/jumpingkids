import flet as ft


class JumpingkidsTheme(ft.Theme):
    pass


class App:
    def __init__(self, theme: JumpingkidsTheme) -> None:
        self._theme = theme
        self._content: ft.Control = ft.Container()
    
    @property
    def theme(self) -> JumpingkidsTheme:
        return self._theme
    
    @property
    def content(self) -> ft.Control:
        return self._content


class TutorFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme) -> None:
        super().__init__(theme)
        


class TutorPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme) -> None:
        super().__init__(theme)



class ChildFreeApp(App):
    def __init__(self, theme: JumpingkidsTheme) -> None:
        super().__init__(theme)


class ChildPremiumApp(App):
    def __init__(self, theme: JumpingkidsTheme) -> None:
        super().__init__(theme)
