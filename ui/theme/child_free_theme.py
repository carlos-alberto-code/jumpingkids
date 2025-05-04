import flet as ft


class ChildFreeTheme(ft.Theme):
    """Tema para el perfil de niño free: tonos morados y cafés, estilo amigable y moderno."""
    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#7C4DFF",  # Morado principal
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#7C4DFF",  # Morado vibrante
                primary_container="#D1C4E9",  # Morado claro
                secondary="#8D6E63",  # Café medio
                tertiary="#FFD180",  # Naranja suave para acentos
                error="#D32F2F",  # Rojo para errores
                background="#F3E5F5",  # Fondo lila claro
                surface="#FFFFFF",  # Superficie blanca
                on_primary="#FFFFFF",  # Texto blanco sobre primario
                on_secondary="#FFFFFF",  # Texto blanco sobre secundario
                on_background="#3E2723",  # Texto café oscuro
                on_surface="#3E2723",  # Texto café oscuro
            ),
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#7C4DFF",
                foreground_color="#FFFFFF",
                elevation=4,
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=3,
                shape=ft.RoundedRectangleBorder(radius=16),
                margin=10,
            ),
            appbar_theme=ft.AppBarTheme(
                bgcolor="#7C4DFF",
                foreground_color="#FFFFFF",
                elevation=0,
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#FFD180",
                text_color="#3E2723",
            ),
            scaffold_bgcolor="#F3E5F5",
            primary_color="#7C4DFF",
        )
