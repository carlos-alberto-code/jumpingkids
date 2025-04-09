import flet as ft

from ui.theme import ChildJumpingKidsTheme

from ui.kids.app_builder import AppViewBuilder
from navigation_system.widget.sidebar import Sidebar, SidebarContent, SidebarGroup, SidebarItem

from domain.application.core.auth import AuthServiceCore
from infrastructure.adapter.auth import AuthRepositoryAdapter


def main(page: ft.Page):

    page.padding = 0
    page.theme = ChildJumpingKidsTheme()
    page.theme_mode = ft.ThemeMode.LIGHT

    auth = AuthServiceCore(AuthRepositoryAdapter())
    user = auth.login("child", "password")
    print(user)

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
