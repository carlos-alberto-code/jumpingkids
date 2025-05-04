import flet as ft

from ui.app.login.login_form import LoginForm
from ui.app.login.signup_form import SignupForm


class AuthPanel(ft.Container):
    """
    Panel que gestiona la visualización de los formularios de autenticación.
    Responsabilidad: solo alternar entre login y signup.
    """
    def __init__(self, on_login=None, on_signup=None):
        super().__init__(
            expand=True,
            padding=ft.padding.all(40),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        )
        self.column_panel = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.content = self.column_panel
        self._build_forms(on_login, on_signup)
        self.show_login()

    def _build_forms(self, on_login, on_signup):
        self.login_form = LoginForm(
            on_login=on_login,
            on_switch_to_signup=lambda e: self.show_signup()
        )
        self.signup_form = SignupForm(
            on_signup=on_signup,
            on_switch_to_login=lambda e: self.show_login()
        )

    @property
    def login_form_instance(self):
        """Permite acceder a la instancia de LoginForm actual."""
        return self.login_form

    def show_login(self):
        self.column_panel.controls = [self.login_form]
        self.content = self.column_panel
        if hasattr(self, "page") and self.page:
            self.page.update()

    def show_signup(self):
        self.column_panel.controls = [self.signup_form]
        self.content = self.column_panel
        if hasattr(self, "page") and self.page:
            self.page.update()
