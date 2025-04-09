import flet as ft


class TutorJumpingKidsTheme(ft.Theme):
    """Tema para el perfil de tutor: más sobrio y profesional, pero conservando identidad."""

    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#4CAF50",  # Mantener consistencia de marca
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#3E8E41",  # Verde ligeramente más oscuro para mayor seriedad
                primary_container="#E8F5E9",  # Mantener consistencia
                secondary="#78909C",  # Gris azulado como acento para profesionalidad
                tertiary="#009688",  # Teal como en el original
                error="#F44336",  # Rojo para errores
                background="#FFFFFF",  # Fondo blanco
                surface="#F5F5F5",  # Superficie ligeramente más oscura
                on_primary="#FFFFFF",
                on_secondary="#FFFFFF",  # Texto blanco para mejor contraste
                on_background="#212121",
                on_surface="#212121",
            ),
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#3E8E41",  # Verde más oscuro
                foreground_color="#FFFFFF",
                elevation=2,  # Menos elevación para diseño más sobrio
                shape=ft.RoundedRectangleBorder(radius=8),  # Bordes menos redondeados
            ),
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=2,  # Menos elevación
                shape=ft.RoundedRectangleBorder(radius=12),  # Bordes moderados
                margin=8,
            ),
            appbar_theme=ft.AppBarTheme(
                bgcolor="#3E8E41",  # Verde más oscuro
                foreground_color="#FFFFFF",
                elevation=0,
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#78909C",  # Gris azulado
                text_color="#FFFFFF",
            ),
            scaffold_bgcolor="#FFFFFF",
            primary_color="#3E8E41",
        )
        