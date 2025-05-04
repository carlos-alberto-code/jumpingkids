import flet as ft

class ChildListComponent(ft.Container):
    """Componente mejorado para mostrar la lista de niños registrados"""
    
    def __init__(self, children_data=None):
        self.children_data = children_data or []
        
        # Mensaje cuando no hay niños
        self.empty_state = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(
                        ft.icons.PERSON_SEARCH,
                        size=40,
                        color="purple200"
                    ),
                    ft.Text(
                        "No hay niños registrados aún",
                        italic=True,
                        color="grey500",
                        text_align=ft.TextAlign.CENTER,
                        size=14
                    ),
                    ft.Text(
                        "Usa el botón 'Agregar hijo' para comenzar",
                        color="grey400",
                        text_align=ft.TextAlign.CENTER,
                        size=12
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            padding=30,
            alignment=ft.alignment.center,
        )
        
        # Lista de niños
        self.list_column = ft.Column(
            spacing=5,
            scroll=ft.ScrollMode.AUTO,
            visible=False if not self.children_data else True,
            height=200,  # Altura fija para evitar desbordamientos
        )
        
        # Mensaje de cuota
        self.quota_text = ft.Text(
            f"0 de 3 cupos utilizados",
            color="grey700",
            size=12,
            text_align=ft.TextAlign.RIGHT
        )
        
        # Actualizar lista y texto de cuota
        self._refresh_list()
        
        # Layout principal
        super().__init__(
            content=ft.Column(
                [
                    # Lista de niños o mensaje de vacío
                    self.list_column,
                    self.empty_state,
                    
                    # Mensaje de cuota
                    ft.Container(
                        content=self.quota_text,
                        padding=ft.padding.only(top=5, right=5),
                        alignment=ft.alignment.center_right
                    )
                ],
                tight=True,
                spacing=5,
            ),
            alignment=ft.alignment.top_center,
            width=400,
            height=250,  # Altura fija para evitar desbordamientos
        )
    
    def _refresh_list(self):
        """Actualiza la lista de niños y el texto de cuota"""
        # Limpiar lista actual
        self.list_column.controls.clear()
        
        # Mostrar estado vacío si no hay niños
        self.empty_state.visible = len(self.children_data) == 0
        self.list_column.visible = len(self.children_data) > 0
        
        # Actualizar texto de cuota
        self.quota_text.value = f"{len(self.children_data)} de 3 cupos utilizados"
        
        # Crear tarjetas para cada niño
        for i, child in enumerate(self.children_data):
            self.list_column.controls.append(self._create_child_card(i, child))
    
    def _create_child_card(self, index, child_data):
        """Crea una tarjeta para un niño registrado"""
        # Determinar color de fondo basado en el índice
        colors = ["#E0BBFF", "#C5CAE9", "#D1C4E9"]
        bg_color = colors[index % len(colors)]
        
        # Crear avatar con iniciales
        initials = "".join([name[0].upper() for name in child_data["full_name"].split() if name])
        if not initials:
            initials = "N"
            
        # Obtener la edad si existe
        age_text = f"{child_data.get('age', '?')} años" if child_data.get('age') else ""
        
        # Crear tarjeta
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
                        # Avatar
                        ft.Container(
                            content=ft.Text(
                                initials,
                                color="white",
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                size=18
                            ),
                            width=40,
                            height=40,
                            border_radius=20,
                            bgcolor="#7C4DFF",
                            alignment=ft.alignment.center,
                        ),
                        
                        # Información del niño
                        ft.Column(
                            [
                                ft.Text(
                                    child_data["full_name"],
                                    weight=ft.FontWeight.BOLD,
                                    size=16
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(
                                            ft.icons.ALTERNATE_EMAIL,
                                            color="grey700",
                                            size=14
                                        ),
                                        ft.Text(
                                            child_data["username"],
                                            color="grey700",
                                            size=14
                                        ),
                                    ],
                                    spacing=5,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                            ],
                            spacing=3,
                            expand=True
                        ),
                        
                        # Badge de edad
                        ft.Container(
                            content=ft.Text(
                                age_text,
                                color="#7C4DFF",
                                size=12,
                                weight=ft.FontWeight.BOLD
                            ),
                            bgcolor="#F3E5F5",
                            border_radius=10,
                            padding=ft.padding.symmetric(horizontal=8, vertical=4),
                            visible=True if age_text else False
                        ),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=10,
            ),
            elevation=0,
            color=bg_color,
            margin=ft.margin.only(bottom=5)
        )
    
    def update(self):
        """Actualiza la visualización del componente"""
        self._refresh_list()
        super().update()