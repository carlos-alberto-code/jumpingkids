import flet as ft

from ui.app.auth.login.auth_panel import AuthPanel
from ui.app.auth.login.animation_panel import AnimationPanel


class AuthView(ft.View):
    
    def __init__(self, on_login=None, on_signup=None):
        self._auth_panel = AuthPanel(on_login=on_login, on_signup=on_signup)
        super().__init__(
            route="/login",
            padding=0,
            controls=[
                ft.Row(
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        AnimationPanel(),
                        self._auth_panel,
                    ],
                    expand=True,
                )
            ],
        )

    @property
    def not_complet_data(self):
        return self._auth_panel.login_form_instance.not_complet_data

    @property
    def username_field(self):
        return self._auth_panel.login_form_instance.username

    @property
    def password_field(self):
        return self._auth_panel.login_form_instance.password

    @property
    def signup(self):
        return self._auth_panel.signup_form_instance
