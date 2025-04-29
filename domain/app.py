import flet as ft


class JumpingkidsTheme(ft.Theme):...


class App:
    def __init__(self, theme: JumpingkidsTheme) -> None:
        self._theme = theme
    
    @property
    def theme(self) -> JumpingkidsTheme:
        return self._theme


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
