import flet as ft
import random

class DailyTipComponent(ft.Container):
    
    TIPS = [
        "Beber agua antes, durante y después de los ejercicios te ayuda a mantenerte hidratado y con más energía.",
        "Hacer 10 minutos de estiramiento antes de ejercitarte puede prevenir lesiones.",
        "Respirar correctamente durante el ejercicio te ayuda a aumentar tu rendimiento.",
        "Descansar bien es tan importante como ejercitarse, duerme al menos 8 horas diarias.",
        "Una buena postura te ayuda a prevenir lesiones y aprovechar mejor tus ejercicios."
    ]
    
    def __init__(self):
        self.tip = random.choice(self.TIPS)
        
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