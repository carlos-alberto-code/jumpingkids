import flet as ft
import random

class DailyTipComponent(ft.Container):
    """Componente que muestra un consejo diario aleatorio al usuario."""
    
    # Lista de consejos predefinidos que se pueden mostrar
    TIPS = [
        "Beber agua antes, durante y después de los ejercicios te ayuda a mantenerte hidratado y con más energía.",
        "Hacer 10 minutos de estiramiento antes de ejercitarte puede prevenir lesiones.",
        "Respirar correctamente durante el ejercicio te ayuda a aumentar tu rendimiento.",
        "Descansar bien es tan importante como ejercitarse, duerme al menos 8 horas diarias.",
        "Una buena postura te ayuda a prevenir lesiones y aprovechar mejor tus ejercicios."
    ]
    
    def __init__(self, tip=None):
        """
        Inicializa el componente de consejo diario.
        
        Args:
            tip (str, opcional): Consejo específico a mostrar. Si es None, se selecciona uno aleatorio.
        """
        self.tip = tip or random.choice(self.TIPS)
        
        # Crear contenido del componente
        content = ft.Column([
            ft.Row([
                ft.Icon(ft.icons.LIGHTBULB, color="#FFD180", size=24),
                ft.Text(
                    "Consejo del día", 
                    size=18, 
                    weight=ft.FontWeight.BOLD, 
                    color="#7C4DFF"
                ),
            ], spacing=10),
            ft.Container(
                content=ft.Text(
                    self.tip,
                    size=14,
                    color="#3E2723",
                ),
                margin=ft.margin.only(top=10),
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
    
    def change_tip(self, new_tip=None):
        """
        Cambia el consejo mostrado.
        
        Args:
            new_tip (str, opcional): Nuevo consejo a mostrar. Si es None, se selecciona aleatoriamente.
        """
        self.tip = new_tip or random.choice([tip for tip in self.TIPS if tip != self.tip])
        
        # Actualizar el texto del consejo
        tip_text = self.content.controls[1].content
        tip_text.value = self.tip
        self.update()
        
    def add_tip(self, tip):
        """
        Añade un nuevo consejo a la lista de consejos disponibles.
        
        Args:
            tip (str): Nuevo consejo a añadir
        """
        if tip and tip not in self.TIPS:
            self.TIPS.append(tip)