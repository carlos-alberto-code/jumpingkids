import flet as ft


class JumpingKidsTheme(ft.Theme):

    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#2196F3",  # Bright blue as seed color
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#2196F3",  # Bright blue for primary elements
                primary_container="#BBDEFB",  # Light blue for containers
                secondary="#FF9800",  # Orange for accent elements
                tertiary="#4CAF50",  # Green for success/progress indicators
                error="#F44336",  # Red for errors
                background="#F5F5F5",  # Light gray background
                surface="#FFFFFF",  # White surface
                on_primary="#FFFFFF",  # White text on primary
                on_secondary="#000000",  # Black text on secondary
                on_background="#000000",  # Black text on background
                on_surface="#000000",  # Black text on surface
            ),
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#4CAF50",  # Green buttons
                foreground_color="#FFFFFF",  # White text
                elevation=4,  # Slightly raised
                shape=ft.RoundedRectangleBorder(radius=12),  # Rounded corners
            ),
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=3,
                shape=ft.RoundedRectangleBorder(radius=16),
                margin=10,
            ),
            appbar_theme=ft.AppBarTheme(
                bgcolor="#2196F3",  # Blue app bar
                foreground_color="#FFFFFF",  # White text
                elevation=0,  # Flat design
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#FF9800",  # Orange badges
                text_color="#FFFFFF",  # White text
            ),
            scaffold_bgcolor="#F5F5F5",  # Light background
            primary_color="#2196F3",  # Blue as primary
        )