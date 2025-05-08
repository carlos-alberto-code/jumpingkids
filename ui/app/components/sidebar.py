import flet as ft

class Sidebar(ft.NavigationRail):
    def __init__(
        self, 
        title="JumpingKids", 
        icon=ft.icons.DIRECTIONS_RUN,
        on_change=None,
    ) -> None:
        self._keys: dict[str, ft.icons] = {}
        self._on_change = on_change
        
        super().__init__(
            selected_index=0,
            extended=True,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=200,
            leading=self._create_leading(title, icon),
            on_change=self._handle_change,
        )
        
        # Inicializar las destinaciones como vacías al principio
        self.destinations = []
    
    def _create_leading(self, title, icon):
        return ft.Container(
            content=ft.Column([
                ft.Row(
                    [
                        ft.Icon(icon, size=24),
                        ft.Text(
                            title, 
                            size=20, 
                            weight=ft.FontWeight.BOLD,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10,
                ),
                ft.Divider(height=1),
            ]),
            margin=ft.margin.only(bottom=10),
            padding=ft.padding.all(10),
        )
    
    def _handle_change(self, e):
        if self._on_change:
            # Obtener la etiqueta actual seleccionada para enviarla al controlador
            labels = list(self._keys.keys())
            if 0 <= e.control.selected_index < len(labels):
                selected_label = labels[e.control.selected_index]
                # Llamar a la función externa con información útil
                self._on_change({
                    "index": e.control.selected_index,
                    "label": selected_label,
                    "icon": self._keys[selected_label]
                })
    
    @property
    def keys(self) -> dict:
        return self._keys

    @keys.setter
    def keys(self, value: dict) -> None:
        """
        Actualiza las claves del menú y recrear los destinos de navegación
        """
        self._keys = value
        self._create_items()
    
    def _create_items(self) -> None:
        """Crea los elementos de navegación a partir del diccionario de claves"""
        self.destinations = [
            ft.NavigationRailDestination(
                icon=ft.Icon(icon),
                selected_icon=ft.Icon(icon),
                label=label,
            ) for label, icon in self._keys.items()
        ]
    
    def set_selected_index(self, index):
        """Establece el elemento seleccionado por índice"""
        if self.destinations:
            if 0 <= index < len(self.destinations):
                self.selected_index = index
                self.update()
    
    def set_selected_by_label(self, label):
        """Establece el elemento seleccionado por etiqueta"""
        if label in self._keys:
            labels = list(self._keys.keys())
            index = labels.index(label)
            self.set_selected_index(index)