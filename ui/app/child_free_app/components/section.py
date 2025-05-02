from turtle import bgcolor
import flet as ft

class SectionHome(ft.Card):
    def __init__(
        self,
        title: str,
        subtitle: str,
        icon,
        icon_bgcolor: str,
        on_click=None,
        margin=ft.margin.only(bottom=16),
        elevation=4,
    ):
        content = ft.Container(
            content=ft.Row([
                ft.Container(
                    content=icon,
                    bgcolor=icon_bgcolor,
                    border_radius=50,
                    padding=12,
                    margin=ft.margin.only(right=16)
                ),
                ft.Column([
                    ft.Text(title, weight=ft.FontWeight.BOLD, size=18, color="D1C4E9"),
                    ft.Text(subtitle, color="grey600", size=14),
                ],
                expand=True)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor="white",
            border_radius=16,
            padding=16,
            border=ft.border.all(3, "D1C4E9"),
            shadow=ft.BoxShadow(blur_radius=4, color="D1C4E9"),
            ink=True,
            on_click=on_click,
        )
        super().__init__(
            content=content,
            margin=margin,
            elevation=elevation,
        )