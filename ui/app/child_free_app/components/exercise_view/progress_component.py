import flet as ft

class ProgressComponent(ft.Container):
    """Componente que muestra la barra de progreso semanal de ejercicios."""
    
    def __init__(self, active_days=2, total_days=7):
        """
        Inicializa el componente de progreso semanal.
        
        Args:
            active_days (int): Número de días activos completados
            total_days (int): Total de días en el período (por defecto 7)
        """
        self.active_days = active_days
        self.total_days = total_days
        self.progress_value = active_days / total_days
        
        # Crear contenido del componente
        content = ft.Column([
            ft.Row([
                ft.Text("Tu progreso semanal", size=16, weight=ft.FontWeight.BOLD, color="green800"),
                ft.Text(f"{active_days}/{total_days} días", size=14, color="green700")
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(
                padding=5,
                content=ft.ProgressBar(
                    value=self.progress_value, 
                    color="green500", 
                    bgcolor="white", 
                    height=15, 
                    width=float("inf")
                ),
            )
        ])
        
        # Inicializar el contenedor con los estilos adecuados
        super().__init__(
            content=content,
            padding=10,
            border_radius=16,
            bgcolor="green100",
            margin=ft.margin.only(bottom=15)
        )
    
    def update_progress(self, active_days=None, total_days=None):
        """
        Actualiza el progreso mostrado en la barra.
        
        Args:
            active_days (int, opcional): Nuevo valor de días activos
            total_days (int, opcional): Nuevo total de días
        """
        if active_days is not None:
            self.active_days = active_days
        
        if total_days is not None:
            self.total_days = total_days
        
        self.progress_value = self.active_days / self.total_days
        
        # Actualizar el texto de días y la barra de progreso
        row = self.content.controls[0] # type: ignore
        row.controls[1].value = f"{self.active_days}/{self.total_days} días"
        
        progress_bar = self.content.controls[1].content # type: ignore
        progress_bar.value = self.progress_value
        
        self.update()