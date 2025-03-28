import flet as ft


class JumpingKidsTheme(ft.Theme):

    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#4CAF50",  # Nature green as seed color
            use_material3=True,
            font_family="Roboto",
            color_scheme=ft.ColorScheme(
                primary="#4CAF50",  # Vibrant green for primary elements
                primary_container="#E8F5E9",  # Light green for containers
                secondary="#8BC34A",  # Light green for accent elements
                tertiary="#009688",  # Teal for complementary highlights
                error="#F44336",  # Red for errors
                background="#FFFFFF",  # Clean white background
                surface="#FAFAFA",  # Off-white surface
                on_primary="#FFFFFF",  # White text on primary
                on_secondary="#000000",  # Black text on secondary
                on_background="#212121",  # Dark text on background
                on_surface="#212121",  # Dark text on surface
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
                bgcolor="#4CAF50",  # Green app bar
                foreground_color="#FFFFFF",  # White text
                elevation=0,  # Flat design
                center_title=True,
            ),
            badge_theme=ft.BadgeTheme(
                bgcolor="#8BC34A",  # Light green badges
                text_color="#FFFFFF",  # White text
            ),
            scaffold_bgcolor="#FFFFFF",  # Clean white background
            primary_color="#4CAF50",  # Green as primary
        )