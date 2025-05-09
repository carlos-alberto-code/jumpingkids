import flet as ft

from domain.model.model import SubscriptionType


class SignupForm(ft.Column):

    def __init__(self, subscription_types: list[SubscriptionType], on_signup=None, on_switch_to_login=None):

        self._full_name_field = ft.TextField(
            label="Nombre completo",
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            height=50,
            width=400,
        )
        self._username_field = ft.TextField(
            label="Nombre de usuario",
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            height=50,
            width=400,
        )
        self._password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            height=50,
            width=400,
        )
        self._subscription_type_field = ft.Dropdown(
            label="Tipo de suscripción",
            options=[
                ft.dropdown.Option(
                    text=subscription_type.name,
                    data=subscription_type
                ) for subscription_type in subscription_types
            ],
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            width=400,
        )
        self._message_text = ft.Text("", color=ft.Colors.RED, visible=False)
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400,
            controls=[
                ft.Text("JUMPINGKIDS", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Crear una cuenta", size=16, color=ft.Colors.GREY_600),
                ft.Container(height=30),
                self._full_name_field,
                self._username_field,
                self._password_field,
                self._subscription_type_field,
                self._message_text,
                ft.ElevatedButton(
                    text="Registrarse",
                    width=400,
                    height=50,
                    on_click=on_signup,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor="#2D2242",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("¿Ya tienes una cuenta?", color=ft.Colors.GREY_600),
                            ft.TextButton(
                                text="Entrar",
                                on_click=on_switch_to_login,
                                style=ft.ButtonStyle(
                                    color="#2D2242",
                                )
                            )
                        ]
                    )
                )
            ]
        )

    @property
    def full_name(self):
        return self._full_name_field.value or ""

    @property
    def username(self):
        return self._username_field.value or ""

    @property
    def password(self):
        return self._password_field.value or ""

    @property
    def subscription_type_id(self):
        return self._subscription_type_field.data.name if self._subscription_type_field.data else 1

    @property
    def completed_data(self):
        return bool(self.full_name.strip() and self.username.strip() and self.password.strip() and self.subscription_type_id)
