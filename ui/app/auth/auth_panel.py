import flet as ft

from domain.model import SubscriptionType
from ui.app.auth.login.login_form import LoginForm
from ui.app.auth.login.signup_form import SignupForm


class AuthPanel(ft.Container):

    def __init__(self, subscription_types: list[SubscriptionType], on_login=None, on_signup=None):
        self._login_form = LoginForm(
            on_login=on_login,
            on_switch_to_signup=lambda e: self.show_signup()
        )
        self._signup_form = SignupForm(
            subscription_types=subscription_types,
            on_signup=on_signup,
            on_switch_to_login=lambda e: self.show_login()
        )

        super().__init__(
            expand=True,
            padding=ft.padding.all(40),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
        )
        self.column_panel = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )
        self.content = self.column_panel
        self.show_login()        
    
    @property
    def login_form(self):
        return self._login_form
    
    @property
    def signup_form(self):
        return self._signup_form

    def show_login(self):
        self.column_panel.controls = [self._login_form]
        self.content = self.column_panel
        # if hasattr(self, "page") and self.page:
        #     self.page.update()

    def show_signup(self):
        self.column_panel.controls = [self.signup_form]
        self.content = self.column_panel
        # if hasattr(self, "page") and self.page:
        #     self.page.update()
