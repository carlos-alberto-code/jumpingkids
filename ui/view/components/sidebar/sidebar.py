import flet as ft

import flet as ft
from ui.view.components.sidebar.sidebar_item import SidebarItem


class Sidebar(ft.Container):
    
    def __init__(self, user_name: str, sidebar_items: list[SidebarItem], on_select=None) -> None:
        self._user_name = user_name
        self._on_select_event = on_select
        self._modules = sidebar_items
        self._module_active = self._modules[0]
        super().__init__(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
                                ft.Text(user_name, color=ft.Colors.WHITE, size=18, weight=ft.FontWeight.BOLD),
                            ]
                        ),
                        padding=10,
                    ),
                    ft.Divider(color=ft.Colors.WHITE24),
                    *sidebar_items,
                    ft.Divider(color=ft.Colors.WHITE24),
                    SidebarItem("Settings", ft.Icons.SETTINGS, on_click=lambda _: print("Settings clicked")),
                    SidebarItem("Help", ft.Icons.HELP, on_click=lambda _: print("Help clicked")),
                    SidebarItem("Logout", ft.Icons.EXIT_TO_APP, on_click=lambda _: print("Logout clicked")),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            width=250,
            bgcolor=ft.Colors.BLUE_GREY_900,
            padding=ft.padding.all(10),
            expand=True,
            
        )
    
    @property
    def user_name(self) -> str:
        return self._user_name
