import flet as ft

class UIMessageService:
    def __init__(self, page):
        self._page = page

    def show_snackbar(self, message: str, bgcolor: str, text_color: str) -> None:
        snackbar = ft.SnackBar(
            content=ft.Row(
                [ft.Text(message, color=text_color, weight=ft.FontWeight.BOLD, size=14)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor=bgcolor,
        )
        self._page.open(snackbar)
