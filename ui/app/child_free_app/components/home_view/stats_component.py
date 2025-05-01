import flet as ft

class StatsComponent(ft.Container):
    """Componente que muestra las estadísticas de progreso del usuario."""
    
    def __init__(self, active_days=2, daily_minutes=15, points=120):
        """
        Inicializa el componente de estadísticas.
        
        Args:
            active_days (int): Número de días activos en la semana
            daily_minutes (int): Minutos de actividad realizados hoy
            points (int): Puntos acumulados por el usuario
        """
        self.active_days = active_days
        self.daily_minutes = daily_minutes
        self.points = points
        
        # Crear contenido del componente
        content = ft.Column([
            ft.Text(
                "Tu progreso semanal", 
                size=18, 
                weight=ft.FontWeight.BOLD, 
                color="#7C4DFF"
            ),
            ft.Row([
                self._create_stat_card(
                    title="Días activos", 
                    value=f"{active_days}/7", 
                    icon=ft.icons.CALENDAR_TODAY
                ),
                self._create_stat_card(
                    title="Minutos hoy", 
                    value=str(daily_minutes), 
                    icon=ft.icons.TIMER,
                    margin=ft.margin.symmetric(horizontal=10)
                ),
                self._create_stat_card(
                    title="Puntos", 
                    value=str(points), 
                    icon=ft.icons.STAR,
                    icon_color="#FFD180"
                ),
            ], 
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=0
            )
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
    
    def _create_stat_card(self, title, value, icon, icon_color="#7C4DFF", margin=None):
        """
        Crea una tarjeta de estadística individual.
        
        Args:
            title (str): Título de la estadística
            value (str): Valor a mostrar
            icon (str): Ícono a mostrar
            icon_color (str): Color del ícono
            margin (ft.margin): Margen del contenedor
            
        Returns:
            ft.Container: Contenedor con la tarjeta de estadística
        """
        return ft.Container(
            content=ft.Column([
                ft.Text(title, size=14, color="#3E2723"),
                ft.Row([
                    ft.Text(
                        value, 
                        size=20, 
                        weight=ft.FontWeight.BOLD, 
                        color="#7C4DFF"
                    ),
                    ft.Icon(icon, size=20, color=icon_color)
                ], spacing=5),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER),
            expand=1,
            padding=10,
            bgcolor="#D1C4E9",
            border_radius=12,
            margin=margin,
            height=80,
        )
    
    def update_stats(self, active_days=None, daily_minutes=None, points=None):
        """
        Actualiza las estadísticas mostradas en el componente.
        
        Args:
            active_days (int): Nuevo valor de días activos
            daily_minutes (int): Nuevo valor de minutos diarios
            points (int): Nuevo valor de puntos
        """
        if active_days is not None:
            self.active_days = active_days
            self._update_card_value(0, f"{active_days}/7")
        
        if daily_minutes is not None:
            self.daily_minutes = daily_minutes
            self._update_card_value(1, str(daily_minutes))
            
        if points is not None:
            self.points = points
            self._update_card_value(2, str(points))
    
    def _update_card_value(self, card_index, new_value):
        """
        Actualiza el valor de una tarjeta específica.
        
        Args:
            card_index (int): Índice de la tarjeta a actualizar
            new_value (str): Nuevo valor a mostrar
        """
        row = self.content.controls[1]
        card = row.controls[card_index]
        value_text = card.content.controls[1].controls[0]
        value_text.value = new_value
        self.update()