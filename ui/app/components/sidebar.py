import flet as ft

class Sidebar(ft.NavigationRail):
    def __init__(self, user_name: str = "Niño/a", avatar_icon: ft.Icon | None = None):
        self._keys: dict[str, ft.Icons] = {}
        self.user_name = user_name
        self.avatar_icon = avatar_icon or ft.Icon(ft.icons.SPORTS_BASKETBALL)
        super().__init__(
            selected_index=0,
            min_width=200,
            width=300,
            extended=True,
            label_type=ft.NavigationRailLabelType.ALL,
        )
        self._build_header()
        self._build_footer()

    def _build_header(self):
        self.leading = ft.Column([
            ft.Container(
                content=self.avatar_icon,
                alignment=ft.alignment.center,
                padding=10,
            ),
            ft.Text(f"¡Hola, {self.user_name}!", size=18, weight=ft.FontWeight.BOLD),
            ft.Text("¡A moverse!", size=14, italic=True),
        ], alignment=ft.MainAxisAlignment.START)

    def _build_footer(self):
        self.trailing = ft.Column([
            ft.IconButton(ft.icons.HELP_OUTLINE, tooltip="Ayuda"),
            ft.IconButton(ft.icons.EXIT_TO_APP, tooltip="Salir"),
        ], alignment=ft.MainAxisAlignment.END)

    @property
    def keys(self) -> dict[str, ft.Icons]:
        return self._keys

    @keys.setter
    def keys(self, values: dict[str, ft.Icons]):
        self._keys = values
        self.update_destinations()

    def update_destinations(self):
        self.destinations = [
            ft.NavigationRailDestination(
                icon=icon,
                label=key
            ) for key, icon in self._keys.items()
        ]
