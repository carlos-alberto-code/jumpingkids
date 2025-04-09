import flet as ft


class ChildJumpingKidsTheme(ft.Theme):
    """Tema para el perfil de niño: más divertido, vibrante y con elementos redondeados."""

    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#4CAF50",  # Mantener el verde base
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#4CAF50",  # Verde vibrante como en el tema original
                primary_container="#E8F5E9",  # Contenedor claro para mantener el diseño fresco
                secondary="#8BC34A",  # Verde más claro para elementos secundarios
                tertiary="#FFEB3B",  # Amarillo para mayor diversión - elemento diferenciador
                error="#F44336",  # Rojo para errores
                background="#FFFFFF",  # Fondo blanco
                surface="#FAFAFA",  # Superficie ligeramente diferente
                on_primary="#FFFFFF",  # Texto blanco sobre primario
                on_secondary="#000000",  # Texto negro sobre secundario
                on_background="#212121",  # Texto oscuro sobre fondo
                on_surface="#212121",  # Texto oscuro sobre superficie
            ),
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#4CAF50",  # Verde para botones
                foreground_color="#FFFFFF",  # Texto blanco
                elevation=5,  # Elevación más pronunciada para efecto lúdico
                shape=ft.RoundedRectangleBorder(radius=16),  # Bordes más redondeados
            ),
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=4,  # Mayor elevación para efecto más pronunciado
                shape=ft.RoundedRectangleBorder(radius=20),  # Esquinas muy redondeadas
                margin=12,
            ),
            appbar_theme=ft.AppBarTheme(
                bgcolor="#4CAF50",  # Verde en la barra
                foreground_color="#FFFFFF",
                elevation=0,
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#FFEB3B",  # Amarillo para resaltar
                text_color="#212121",  # Texto negro para mejor contraste
            ),
            scaffold_bgcolor="#FFFFFF",
            primary_color="#4CAF50",
        )
