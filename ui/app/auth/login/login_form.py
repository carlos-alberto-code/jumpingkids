import flet as ft


class LoginForm(ft.Column):
    def __init__(self, on_login=None, on_switch_to_signup=None):
        self.username_field = ft.TextField(
            label="Nombre de usuario",
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            height=50,
            width=400,
        )
        self.password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=8,
            filled=True,
            bgcolor=ft.Colors.GREY_100,
            height=50,
            width=400,
        )
        self.message_text = ft.Text("", color=ft.Colors.RED, visible=False)
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400,
            controls=[
                ft.Text("JUMPINGKIDS", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Bienvenido de Vuelta", size=16, color=ft.Colors.GREY_600),
                ft.Container(height=30),
                self.username_field,
                self.password_field,
                self.message_text,
                ft.Container(height=10),
                ft.ElevatedButton(
                    text="Iniciar sesión",
                    width=400,
                    height=50,
                    on_click=on_login,
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
                            ft.Text("¿No tienes una cuenta?", color=ft.Colors.GREY_600),
                            ft.TextButton(
                                text="Registrarse",
                                on_click=on_switch_to_signup,
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
    def username(self):
        return self.username_field.value or ""

    @property
    def password(self):
        return self.password_field.value or ""

    @property
    def not_complet_data(self):
        """Retorna True si falta algún dato requerido."""
        return not self.username.strip() or not self.password.strip()

    def show_message(self, message):
        self.message_text.value = message
        self.message_text.visible = True
        if hasattr(self, "page") and self.page:
            self.page.update()
