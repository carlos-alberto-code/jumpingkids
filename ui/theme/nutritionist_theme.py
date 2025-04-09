import flet as ft


class NutritionistJumpingKidsTheme(ft.Theme):
    """Tema para el perfil de nutricionista: equilibrio entre profesionalidad y salud."""

    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#4CAF50",  # Mantener consistencia de marca
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#2E7D32",  # Verde oscuro para profesionalidad
                primary_container="#E8F5E9",
                secondary="#FF9800",  # Naranja para representar vitalidad y nutrición
                tertiary="#3F51B5",  # Azul índigo como acento diferenciador
                error="#F44336",
                background="#FFFFFF",
                surface="#FAFAFA",
                on_primary="#FFFFFF",
                on_secondary="#000000",
                on_background="#212121",
                on_surface="#212121",
            ),
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#2E7D32",  # Verde oscuro
                foreground_color="#FFFFFF",
                elevation=3,
                shape=ft.RoundedRectangleBorder(radius=10),  # Bordes intermedios
            ),
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=2,
                shape=ft.RoundedRectangleBorder(radius=14),
                margin=10,
            ),
            appbar_theme=ft.AppBarTheme(
                bgcolor="#2E7D32",  # Verde oscuro
                foreground_color="#FFFFFF",
                elevation=0,
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#FF9800",  # Naranja
                text_color="#FFFFFF",
            ),
            scaffold_bgcolor="#FFFFFF",
            primary_color="#2E7D32",
        )
