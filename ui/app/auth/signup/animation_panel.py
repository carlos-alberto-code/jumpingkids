import flet as ft


class AnimationWidget(ft.Container):
    """Componente para mostrar la animación Lottie."""
    def __init__(self, animation_url: str):
        super().__init__(
            content=ft.Lottie(
                animation_url,
                width=250,
                height=250,
                repeat=True,
                animate=True,
            ),
            alignment=ft.alignment.center,
            margin=ft.margin.symmetric(vertical=20),
        )


class MotivationalTextList(ft.Column):
    """Componente para mostrar una lista de textos motivacionales como tarjetas."""
    def __init__(self, texts: list[str]):
        super().__init__(
            [self._create_motivational_card(text) for text in texts],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def _create_motivational_card(self, text: str) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(
                        ft.icons.CHECK_CIRCLE_ROUNDED,
                        color="white",
                        size=16,
                    ),
                    ft.Text(
                        text,
                        color="white",
                        size=14,
                        weight=ft.FontWeight.W_500,
                        max_lines=None,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.symmetric(vertical=5),
            padding=ft.padding.all(10),
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.colors.with_opacity(0.15, "white"),
            width=None,
            expand=True,
        )


class BrandingPanel(ft.Container):
    """Componente para mostrar el logo y subtítulo de la app."""
    def __init__(self):
        super().__init__(
            content=ft.Column(
                [
                    ft.Text(
                        "JumpingKids",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                    ),
                    ft.Text(
                        "Haciendo niños activos",
                        size=12,
                        color="white",
                        opacity=0.7,
                    ),
                ],
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=40),
            alignment=ft.alignment.center,
        )


class AnimationPanel(ft.Container):
    """
    Panel de animación que orquesta los componentes de animación, textos motivacionales y branding.
    """
    def __init__(self):
        animation_url = "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json"
        motivational_text = [
            "¡Haz que tus hijos se ejerciten divirtiéndose!",
            "Actividad física + diversión = niños saludables",
            "Acompaña a tus hijos en su desarrollo físico",
            "¡Cada salto cuenta para una vida activa!",
            "Fomenta hábitos saludables desde pequeños",
        ]
        super().__init__(
            content=ft.Column(
                [
                    ft.Text(
                        "¡Bienvenido a JumpingKids!",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Un lugar divertido para ejercitarse",
                        size=16,
                        italic=True,
                        color="white",
                        opacity=0.8,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    AnimationWidget(animation_url),
                    MotivationalTextList(motivational_text),
                    BrandingPanel(),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
                expand=True,
            ),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.only(
                top_right=24,
                bottom_right=24
            ),
            gradient=None,
            padding=30,
            expand=True,
            width=420,
            bgcolor="#2D2242",
        )