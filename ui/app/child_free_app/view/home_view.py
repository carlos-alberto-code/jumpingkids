import flet as ft
from ui.app.child_free_app.components.section import SectionHome
from ui.app.components.appbar import JumpingKidsAppbar
from ui.app.child_free_app.components.challenge_card import PremiumBanner

class HomeView(ft.View):
    def __init__(self):

        # Crear componentes de la vista
        welcome_container = self._create_welcome_container(username="Alberto")
        sections_container = self._create_sections_container()
        stats_container = self._create_stats_container()
        daily_tip_container = self._create_daily_tip_container()

        super().__init__(
            route="/home",
            appbar=None,
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.ListView(
                        [
                            welcome_container,
                            stats_container,
                            sections_container,
                            daily_tip_container,
                            PremiumBanner()
                        ],
                        spacing=15,
                        padding=20,
                    )
                )
            ],
            bgcolor="#F3E5F5",  # Color de fondo lila claro como en ChildFreeTheme
        )

    def _create_welcome_container(self, username):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([
                        ft.Text(
                            f"¡Hola, {username}!", 
                            size=26, 
                            weight=ft.FontWeight.BOLD, 
                            color="#7C4DFF"  # Morado principal
                        ),
                        ft.Text(
                            "¿Listo para divertirte ejercitándote hoy?", 
                            size=16, 
                            color="#3E2723",  # Texto café oscuro
                            weight=ft.FontWeight.W_400
                        ),
                    ], expand=True),
                    ft.Container(
                        # height=200,
                        content=ft.Lottie(
                            "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json",
                            width=100,
                            height=100,
                            repeat=True,
                            animate=True
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=10, bottom=20),
                    )
                ]),
            ]),
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )

    def _create_stats_container(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "Tu progreso semanal", 
                    size=18, 
                    weight=ft.FontWeight.BOLD, 
                    color="#7C4DFF"
                ),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Días activos", size=14, color="#3E2723"),
                            ft.Row([
                                ft.Text(
                                    "2/7", 
                                    size=20, 
                                    weight=ft.FontWeight.BOLD, 
                                    color="#7C4DFF"
                                ),
                                ft.Icon(ft.icons.CALENDAR_TODAY, size=20, color="#7C4DFF")
                            ], spacing=5),
                        ], 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER),
                        expand=1,
                        padding=10,
                        bgcolor="#D1C4E9",
                        border_radius=12,
                        height=80,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Minutos hoy", size=14, color="#3E2723"),
                            ft.Row([
                                ft.Text(
                                    "15", 
                                    size=20, 
                                    weight=ft.FontWeight.BOLD, 
                                    color="#7C4DFF"
                                ),
                                ft.Icon(ft.icons.TIMER, size=20, color="#7C4DFF")
                            ], spacing=5),
                        ], 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER),
                        expand=1,
                        padding=10,
                        bgcolor="#D1C4E9",
                        border_radius=12,
                        margin=ft.margin.symmetric(horizontal=10),
                        height=80,
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("Puntos", size=14, color="#3E2723"),
                            ft.Row([
                                ft.Text(
                                    "120", 
                                    size=20, 
                                    weight=ft.FontWeight.BOLD, 
                                    color="#7C4DFF"
                                ),
                                ft.Icon(ft.icons.STAR, size=20, color="#FFD180")
                            ], spacing=5),
                        ], 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER),
                        expand=1,
                        padding=10,
                        bgcolor="#D1C4E9",
                        border_radius=12,
                        height=80,
                    ),
                ], 
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=0,
                )
            ]),
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )

    def _create_sections_container(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(
                    "Actividades", 
                    size=18, 
                    weight=ft.FontWeight.BOLD, 
                    color="#7C4DFF"
                ),
                SectionHome(
                    title="Ejercicios diarios",
                    subtitle="¡Actívate con ejercicios divertidos!",
                    icon=ft.Icon(ft.icons.FITNESS_CENTER, color="#7C4DFF", size=40),
                    icon_bgcolor="#D1C4E9",
                    on_click=lambda e: self._on_section_click("/ejercicios"),
                    margin=ft.margin.only(top=10, bottom=10),
                ),
                SectionHome(
                    title="Desafíos semanales",
                    subtitle="Supera retos y gana medallas",
                    icon=ft.Icon(ft.icons.STAR, color="#FFD180", size=40),
                    icon_bgcolor="#FFF3E0",
                    on_click=lambda e: self._on_section_click("/desafios"),
                    margin=ft.margin.only(bottom=10),
                ),
                SectionHome(
                    title="Mi personaje",
                    subtitle="Personaliza tu avatar y mira tus logros",
                    icon=ft.Icon(ft.icons.PERSON, color="#7C4DFF", size=40),
                    icon_bgcolor="#D1C4E9",
                    on_click=lambda e: self._on_section_click("/personajes"),
                ),
            ]),
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )

    def _create_daily_tip_container(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.LIGHTBULB, color="#FFD180", size=24),
                    ft.Text(
                        "Consejo del día", 
                        size=18, 
                        weight=ft.FontWeight.BOLD, 
                        color="#7C4DFF"
                    ),
                ], spacing=10),
                ft.Container(
                    content=ft.Text(
                        "Beber agua antes, durante y después de los ejercicios te ayuda a mantenerte hidratado y con más energía.",
                        size=14,
                        color="#3E2723",
                    ),
                    margin=ft.margin.only(top=10),
                ),
            ]),
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )


    def _on_section_click(self, route):
        if self.page:
            self.page.go(route)

    def _on_nav_bar_change(self, e):
        index = e.control.selected_index
        routes = ["/home", "/ejercicios", "/desafios", "/personajes"]
        if self.page and index < len(routes):
            self.page.go(routes[index])