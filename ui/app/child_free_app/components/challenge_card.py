import flet as ft

class ChallengeCard(ft.Container):
    def __init__(self, nombre, descripcion, personaje, dias, medalla):
        super().__init__(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(ft.icons.STAR, color="#FFB800", size=28),
                    bgcolor="yellow100", border_radius=50, padding=8, margin=ft.margin.only(right=10)
                ),
                ft.Column([
                    ft.Text(nombre, weight=ft.FontWeight.BOLD, size=18),
                    ft.Text(descripcion, color="grey600", size=14),
                    ft.Row([
                        ft.Icon(ft.icons.PERSON, color="blue500", size=16),
                        ft.Text(personaje, size=14, color="blue500")
                    ], spacing=5),
                    ft.Row([
                        ft.Container(
                            content=ft.Text(f"{dias} días", size=12, color="orange800", weight=ft.FontWeight.BOLD),
                            bgcolor="orange100", border_radius=8, padding=5
                        ),
                        ft.Row([
                            ft.Icon(ft.icons.MILITARY_TECH, color="amber600", size=16),
                            ft.Text(f"Medalla de {medalla}", size=12, color="amber600")
                        ], spacing=3)
                    ], alignment=ft.MainAxisAlignment.START)
                ], expand=True)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor="white", border_radius=16, padding=16, margin=ft.margin.only(bottom=10), border=ft.border.all(2, "green100"), shadow=ft.BoxShadow(blur_radius=4, color="grey100")
        )

class PremiumBanner(ft.Container):
    def __init__(self):
        super().__init__(
            margin=ft.margin.only(top=10),
            bgcolor="green50", border_radius=12, padding=12,
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(ft.icons.KEYBOARD_DOUBLE_ARROW_UP, color="green600", size=20),
                    bgcolor="green100", border_radius=50, padding=8, margin=ft.margin.only(right=10)
                ),
                ft.Text("¡Obtén más desafíos con el plan premium!", color="green800", size=14, weight=ft.FontWeight.W_100),
                ft.Container(
                    content=ft.Text("Actualizar", color="white", size=12, weight=ft.FontWeight.W_100),
                    bgcolor="green500", border_radius=50, padding=ft.padding.symmetric(horizontal=12, vertical=6)
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        )
