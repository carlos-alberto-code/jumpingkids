import flet as ft

class ChildFreeTheme(ft.Theme):
    """
    Tema JumpingKids: paleta UX optimizada para niños de 10-15 años, ejercicio y vitalidad.
    Azul energético, verde vitalidad, naranja dinámico y neutros accesibles.
    """
    def __init__(self) -> None:
        super().__init__(
            color_scheme_seed="#1E88E5",  # Azul energético
            use_material3=True,
            font_family="Roboto",

            # Esquema de colores armónico y energético
            color_scheme=ft.ColorScheme(
                primary="#1E88E5",            # Azul energético
                primary_container="#64B5F6",  # Azul claro
                secondary="#43A047",          # Verde vitalidad
                secondary_container="#81C784", # Verde claro
                tertiary="#FB8C00",           # Naranja dinámico
                tertiary_container="#FFCC80", # Naranja claro
                error="#F44336",              # Rojo corrección
                error_container="#FFEBEE",    # Rojo claro
                background="#FFFFFF",         # Fondo principal
                surface="#E3F2FD",            # Fondo secundario (azul pálido)
                surface_variant="#ECEFF1",    # Gris muy claro para bordes y paneles
                on_primary="#FFFFFF",         # Texto sobre azul
                on_primary_container="#1565C0", # Texto sobre azul claro
                on_secondary="#FFFFFF",       # Texto sobre verde
                on_secondary_container="#2E7D32", # Texto sobre verde claro
                on_tertiary="#FFFFFF",        # Texto sobre naranja
                on_tertiary_container="#EF6C00", # Texto sobre naranja oscuro
                on_error="#FFFFFF",           # Texto sobre error
                on_error_container="#B71C1C", # Texto sobre error_container
                on_background="#263238",      # Texto principal
                on_surface="#263238",         # Texto sobre superficie
                on_surface_variant="#607D8B", # Texto secundario
                shadow="#64B5F6",             # Sombra azul claro
                outline="#ECEFF1",            # Bordes
            ),

            # Tema para botones elevados (primarios)
            elevated_button_theme=ft.ElevatedButtonTheme(
                bgcolor="#1E88E5",
                foreground_color="#FFFFFF",
                elevation=3,
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
            ),

            # Tema para botones secundarios
            filled_button_theme=ft.FilledButtonTheme(
                bgcolor="#43A047",
                foreground_color="#FFFFFF",
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
            ),

            # Tema para botones de acento
            text_button_theme=ft.TextButtonTheme(
                foreground_color="#FB8C00", 
                shape=ft.RoundedRectangleBorder(radius=8),
            ),

            # Tema para tarjetas y paneles
            card_theme=ft.CardTheme(
                color="#FFFFFF",
                elevation=2,
                shape=ft.RoundedRectangleBorder(radius=16),
                margin=12,
                shadow_color="#64B5F6",
            ),

            # Tema para barra de aplicación
            appbar_theme=ft.AppBarTheme(
                bgcolor="#1E88E5",
                foreground_color="#FFFFFF",
                elevation=0,
                center_title=True,
                shadow_color="transparent",
            ),

            # Tema para distintivos (badges)
            badge_theme=ft.BadgeTheme(
                bgcolor="#FB8C00",
                text_color="#FFFFFF",
                padding=ft.padding.symmetric(horizontal=8, vertical=2),
            ),

            # Tema para barras de navegación
            navigation_bar_theme=ft.NavigationBarTheme(
                # No se definen parámetros personalizados, usar color_scheme para colores
            ),

            # Tema para barras de navegación lateral (NavigationRail)
            navigation_rail_theme=ft.NavigationRailTheme(
                bgcolor="#E3F2FD",
                selected_label_text_style=ft.TextStyle(color="#1E88E5", weight=ft.FontWeight.BOLD),
                unselected_label_text_style=ft.TextStyle(color="#607D8B"),
                group_alignment=-0.9,  # Alinear elementos hacia arriba
                label_type=ft.NavigationRailLabelType.ALL,
                min_width=80,
                min_extended_width=220,
                elevation=1,
            ),

            # Tema para cajones de navegación (NavigationDrawer)
            navigation_drawer_theme=ft.NavigationDrawerTheme(
                bgcolor="#FFFFFF",
                # Otros parámetros no válidos eliminados
            ),

            # Tema para divisores
            divider_theme=ft.DividerTheme(
                color="#ECEFF1",
                thickness=1,
            ),

            # Tema para iconos
            icon_theme=ft.IconTheme(
                color="#607D8B",
                size=24,
            ),

            # Propiedades generales del tema
            scaffold_bgcolor="#FFFFFF",
            primary_color="#1E88E5",
            shadow_color="#64B5F6",
        )