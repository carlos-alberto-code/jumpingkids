import flet as ft

class SectionHome(ft.Card):

    def __init__(self, title: str, lottie: ft.Lottie, on_click=None):
        super().__init__(
            content=ft.Column(
                [
                    ft.Stack(
                        controls=[
                            ft.Container(
                                content=lottie,
                                width=100,
                                height=100,
                                alignment=ft.alignment.center,
                            ),
                            ft.Text(
                                title,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ]
                    )
                ],
                spacing=10,
            ),
        )