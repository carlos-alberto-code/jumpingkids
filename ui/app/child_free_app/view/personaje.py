import flet as ft

class PersonajeView(ft.View):
    def __init__(self):
        super().__init__(
            route="/personaje",
            controls=[
                ft.Container(
                    padding=20,
                    content=ft.Column([
                        ft.Text("Tu personaje", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                        ft.Container(
                            bgcolor="white", border_radius=16, padding=24, border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100"),
                            content=ft.Column([
                                ft.Container(
                                    content=ft.Icon(ft.icons.PERSON, color="white", size=48),
                                    bgcolor="green500", border_radius=50, width=96, height=96, alignment=ft.alignment.center, margin=ft.margin.only(bottom=16)
                                ),
                                ft.Text("Aventurero Inicial", weight=ft.FontWeight.BOLD, size=20),
                                ft.Text("¡Personaliza tu avatar y comienza tu aventura de ejercicios!", color="grey600", size=14, text_align=ft.TextAlign.CENTER),
                                ft.Row([
                                    ft.Container(
                                        bgcolor="green50", border_radius=12, padding=12,
                                        content=ft.Column([
                                            ft.Icon(ft.icons.MILITARY_TECH, color="amber600", size=24),
                                            ft.Text("2 medallas ganadas", size=12, color="green800", text_align=ft.TextAlign.CENTER)
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                                    ),
                                    ft.Container(
                                        bgcolor="green50", border_radius=12, padding=12,
                                        content=ft.Column([
                                            ft.Icon(ft.icons.STAR, color="blue600", size=24),
                                            ft.Text("Nivel 1", size=12, color="green800", text_align=ft.TextAlign.CENTER)
                                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                                    )
                                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                                ft.Container(
                                    content=ft.Text("Personalizar avatar", color="white", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                                    bgcolor="green500", border_radius=8, padding=ft.padding.symmetric(vertical=12), width=float("inf")
                                ),
                                ft.Container(
                                    margin=ft.margin.only(top=16),
                                    bgcolor="amber50", border_radius=12, padding=12,
                                    content=ft.Row([
                                        ft.Container(
                                            content=ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_UP, color="amber600", size=20),
                                            bgcolor="amber100", border_radius=50, padding=8, margin=ft.margin.only(right=10)
                                        ),
                                        ft.Text("Más opciones de personalización en plan premium", color="amber800", size=14)
                                    ])
                                )
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                        )
                    ])
                )
            ]
        )
