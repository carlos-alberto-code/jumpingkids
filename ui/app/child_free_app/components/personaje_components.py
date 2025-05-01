import flet as ft

class AvatarCard(ft.Container):
    def __init__(self, nombre, descripcion):
        super().__init__(
            bgcolor="white", border_radius=16, padding=24, border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100"),
            content=ft.Column([
                ft.Container(
                    content=ft.Icon(ft.icons.PERSON, color="white", size=48),
                    bgcolor="green500", border_radius=50, width=96, height=96, alignment=ft.alignment.center, margin=ft.margin.only(bottom=16)
                ),
                ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(descripcion, color="grey600", size=14, text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

class AchievementSummary(ft.Row):
    def __init__(self, medallas, nivel):
        super().__init__(
            [
                ft.Container(
                    bgcolor="green50", border_radius=12, padding=12,
                    content=ft.Column([
                        ft.Icon(ft.icons.MILITARY_TECH, color="amber600", size=24),
                        ft.Text(f"{medallas} medallas ganadas", size=12, color="green800", text_align=ft.TextAlign.CENTER)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                ),
                ft.Container(
                    bgcolor="green50", border_radius=12, padding=12,
                    content=ft.Column([
                        ft.Icon(ft.icons.STAR, color="blue600", size=24),
                        ft.Text(f"Nivel {nivel}", size=12, color="green800", text_align=ft.TextAlign.CENTER)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )

class PremiumBannerPersonaje(ft.Container):
    def __init__(self):
        super().__init__(
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
