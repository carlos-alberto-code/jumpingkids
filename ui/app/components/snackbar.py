import flet as ft


class JSnackbar(ft.SnackBar):

    def __init__(self, message: str, bgcolor: str, text_color: str):
        super().__init__(
            content=ft.Row(
                [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
        )
        