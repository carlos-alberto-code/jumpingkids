import flet as ft
from ui.app.child_free_app.components.section import SectionHome

class SectionsComponent(ft.Container):
    """Componente que muestra las actividades disponibles para el usuario."""
    
    def __init__(self, on_section_click=None):
        """
        Inicializa el componente de secciones/actividades.
        
        Args:
            on_section_click (callable): Función a ejecutar cuando se hace clic en una sección
        """
        self.on_section_click = on_section_click or (lambda route: None)
        
        # Crear contenido del componente
        content = ft.Column([
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
                on_click=lambda e: self.on_section_click("/ejercicios"),
                margin=ft.margin.only(top=10, bottom=10),
            ),
            SectionHome(
                title="Desafíos semanales",
                subtitle="Supera retos y gana medallas",
                icon=ft.Icon(ft.icons.STAR, color="#FFD180", size=40),
                icon_bgcolor="#FFF3E0",
                on_click=lambda e: self.on_section_click("/desafios"),
                margin=ft.margin.only(bottom=10),
            ),
            SectionHome(
                title="Mi personaje",
                subtitle="Personaliza tu avatar y mira tus logros",
                icon=ft.Icon(ft.icons.PERSON, color="#7C4DFF", size=40),
                icon_bgcolor="#D1C4E9",
                on_click=lambda e: self.on_section_click("/personajes"),
            ),
        ])
        
        # Inicializar el contenedor con los estilos adecuados
        super().__init__(
            content=content,
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )
    
    def add_section(self, title, subtitle, icon, icon_bgcolor, route, margin=None):
        """
        Añade una nueva sección al componente.
        
        Args:
            title (str): Título de la sección
            subtitle (str): Subtítulo o descripción
            icon (ft.Icon): Icono a mostrar
            icon_bgcolor (str): Color de fondo del icono
            route (str): Ruta a navegar al hacer clic
            margin (ft.margin): Márgenes del componente
        """
        new_section = SectionHome(
            title=title,
            subtitle=subtitle,
            icon=icon,
            icon_bgcolor=icon_bgcolor,
            on_click=lambda e: self.on_section_click(route),
            margin=margin,
        )
        self.content.controls.append(new_section)
        self.update()
        
    def set_on_section_click(self, callback):
        """
        Actualiza la función callback para manejar clicks en las secciones.
        
        Args:
            callback (callable): Nueva función a ejecutar cuando se hace clic
        """
        self.on_section_click = callback
        
        # Actualizar los callbacks en todas las secciones existentes
        for i in range(1, len(self.content.controls)):
            section = self.content.controls[i]
            if hasattr(section, 'on_click'):
                # Obtener la ruta del evento actual
                route = None
                if section.on_click:
                    old_callback = section.on_click
                    # Extraer la ruta del lambda original (esto es una simplificación)
                    if hasattr(old_callback, '__closure__') and old_callback.__closure__:
                        for cell in old_callback.__closure__:
                            if isinstance(cell.cell_contents, str) and cell.cell_contents.startswith('/'):
                                route = cell.cell_contents
                                break
                
                if route:
                    section.on_click = lambda e, r=route: callback(r)
        
        self.update()