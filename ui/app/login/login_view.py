import flet as ft
from .animation_panel import AnimationPanel
from .auth_panel import AuthPanel

class LoginView(ft.View):
    """
    Vista principal de login/signup.
    Responsabilidad: organizar la estructura visual principal.
    """
    def __init__(self, on_login=None, on_signup=None):
        super().__init__(
            route="/login",
            padding=0,
            controls=[
                ft.Row(
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        AnimationPanel(),
                        AuthPanel(on_login=on_login, on_signup=on_signup),
                    ],
                    expand=True,
                )
            ],
        )
