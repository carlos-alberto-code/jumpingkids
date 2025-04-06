import flet as ft

from ui.kids.app_builder import AppViewBuilder
from ui.kids.view.theme import JumpingKidsTheme

from navigation_system.widget.sidebar import Sidebar, SidebarContent, SidebarGroup, SidebarItem


def main(page: ft.Page):

    page.padding = 0
    page.theme = JumpingKidsTheme()
    page.theme_mode = ft.ThemeMode.LIGHT

    sidebar_content = SidebarContent(
        groups=[
            SidebarGroup(
                title="Kids",
                items=[
                    SidebarItem(
                        icon=ft.Icons.HOME,
                        name="Home",
                    ),
                    SidebarItem(
                        icon=ft.Icons.PERSON,
                        name="Profile",
                    ),
                    SidebarItem(
                        icon=ft.Icons.SETTINGS,
                        name="Settings",
                    ),
                ],
            )
        ]
    )
    page.add(
        Sidebar(
            sidebar_content=sidebar_content,
            company_name="Jumpingkids",
        )
    )


ft.app(target=main, port=9000)
