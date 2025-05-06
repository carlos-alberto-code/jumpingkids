import flet as ft


class ChildListComponent(ft.Container):
    """Componente mejorado para mostrar la lista de niños registrados con colores modernos y consistentes con LoginView."""
    
    def __init__(self, children_data=None):
        self.children_data = children_data or []
        
        # Mensaje cuando no hay niños
        self.empty_state = ft.Container(
            content=ft.Column(
                [
                    ft.Icon(
                        ft.icons.PERSON_SEARCH,
                        size=40,
                        color="#7C4DFF"  # Morado principal
                    ),
                    ft.Text(
                        "No hay niños registrados aún",
                        italic=True,
                        color=ft.Colors.GREY_600,
                        text_align=ft.TextAlign.CENTER,
                        size=14
                    ),
                    ft.Text(
                        "Usa el botón 'Agregar hijo' para comenzar",
                        color=ft.Colors.GREY_400,
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
            height=200,
        )
        
        # Mensaje de cuota
        self.quota_text = ft.Text(
            f"0 de 3 cupos utilizados",
            color=ft.Colors.GREY_700,
            size=12,
            text_align=ft.TextAlign.RIGHT
        )
        
        self._refresh_list()
        
        super().__init__(
            content=ft.Column(
                [
                    self.list_column,
                    self.empty_state,
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
            height=250,
            bgcolor=ft.Colors.GREY_100,  # Fondo igual que el login
            border_radius=12,
            shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.with_opacity(0.08, "#2D2242")),
        )
    
    def _refresh_list(self):
        self.list_column.controls.clear()
        self.empty_state.visible = len(self.children_data) == 0
        self.list_column.visible = len(self.children_data) > 0
        self.quota_text.value = f"{len(self.children_data)} de 3 cupos utilizados"
        for i, child in enumerate(self.children_data):
            self.list_column.controls.append(self._create_child_card(i, child))
    
    def _create_child_card(self, index, child_data):
        # Paleta moderna: alterna entre blanco y lila claro
        colors = [ft.Colors.WHITE, "#F3E5F5", "#EDE7F6"]
        bg_color = colors[index % len(colors)]
        initials = "".join([name[0].upper() for name in child_data["full_name"].split() if name]) or "N"
        age_text = f"{child_data.get('age', '?')} años" if child_data.get('age') else ""
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
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
                            bgcolor="#2D2242",  # Avatar igual que login
                            alignment=ft.alignment.center,
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    child_data["full_name"],
                                    weight=ft.FontWeight.BOLD,
                                    size=16,
                                    color="#2D2242"
                                ),
                                ft.Row(
                                    [
                                        ft.Icon(
                                            ft.icons.ALTERNATE_EMAIL,
                                            color=ft.Colors.GREY_700,
                                            size=14
                                        ),
                                        ft.Text(
                                            child_data["username"],
                                            color=ft.Colors.GREY_700,
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
                        ft.Container(
                            content=ft.Text(
                                age_text,
                                color="#2D2242",
                                size=12,
                                weight=ft.FontWeight.BOLD
                            ),
                            bgcolor="#D1C4E9",
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
        self._refresh_list()
        super().update()