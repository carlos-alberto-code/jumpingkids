import flet as ft


class Navigation(ft.NavigationBar):

    def __init__(self) -> None:
        super().__init__(
            destinations=[
                ft.NavigationBarDestination(
                    label="Rutinas",
                    icon=ft.Icons.FITNESS_CENTER,
                ),
                ft.NavigationBarDestination(
                    label="Ejercicios",
                    icon=ft.Icons.FITNESS_CENTER,
                ),
                ft.NavigationBarDestination(
                    label="Favoritos",
                    icon=ft.Icons.FAVORITE,
                ),
                ft.NavigationBarDestination(
                    label="Categorías",
                    icon=ft.Icons.CATEGORY,
                ),
                ft.NavigationBarDestination(
                    label="Perfil",
                    icon=ft.Icons.PERSON,
                ),
            ]
        )
        