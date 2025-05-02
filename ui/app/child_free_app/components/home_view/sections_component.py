import flet as ft
from ui.app.child_free_app.components.section import SectionHome

class SectionsComponent(ft.Container):
    """Componente que muestra las actividades disponibles para el usuario."""
    
    def __init__(self, on_exercise_click=None, on_challenges_click=None, on_personaje_click=None):
        self.on_exercise_click = on_exercise_click
        self.on_challenges_click = on_challenges_click
        self.on_personaje_click = on_personaje_click
        
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
                on_click=self.on_exercise_click,
                margin=ft.margin.only(top=10, bottom=10),
            ),
            SectionHome(
                title="Desafíos semanales",
                subtitle="Supera retos y gana medallas",
                icon=ft.Icon(ft.icons.STAR, color="#7C4DFF", size=40),
                icon_bgcolor="#D1C4E9",
                on_click=self.on_challenges_click,
                margin=ft.margin.only(bottom=10),
            ),
            SectionHome(
                title="Mi personaje",
                subtitle="Personaliza tu avatar y mira tus logros",
                icon=ft.Icon(ft.icons.PERSON, color="#7C4DFF", size=40),
                icon_bgcolor="#D1C4E9",
                on_click=self.on_personaje_click,
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
