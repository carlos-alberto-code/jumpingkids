import flet as ft

class SignupForm(ft.Column):
    def __init__(self, on_signup=None, on_switch_to_login=None):
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400,
            controls=[
                ft.Text("JUMPINGKIDS", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Crear una cuenta", size=16, color=ft.Colors.GREY_600),
                ft.Container(height=30),
                ft.TextField(
                    label="Nombre completo",
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.TextField(
                    label="Confirmar Contraseña",
                    password=True,
                    can_reveal_password=True,
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
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
