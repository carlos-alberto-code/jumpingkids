import flet as ft


class Sidebar(ft.NavigationRail):
    def __init__(self):
        self._keys: dict[str, ft.Icons] = {}
        super().__init__(
            selected_index=0,
            min_width=200,
            width=300,
            extended=True,
            label_type=ft.NavigationRailLabelType.ALL,
        )
    
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
        