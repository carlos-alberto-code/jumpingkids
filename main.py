import flet as ft

from domain.login import LoginServiceCore
from infrastructure.login import LoginRepositoryAdapter
from domain.subscription import SubscriptionServiceCore
from ui.subscription.subscription_gui_adapter import SubscriptionGuiAdapter

from navigation_system.widget.sidebar import Sidebar, SidebarContent, SidebarGroup, SidebarItem


def main(page: ft.Page):

    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    user = LoginServiceCore(LoginRepositoryAdapter()).login("cabh", "cabh")
    print(user)

    if not user:
        raise ValueError("No se pudo iniciar sesión con las credenciales proporcionadas.")
    
    app = SubscriptionServiceCore(SubscriptionGuiAdapter()).get_user_app(user)
    page.theme = app.theme

    

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
            ),
            SidebarGroup(
                title="Games",
                items=[
                    SidebarItem(
                        icon=ft.Icons.GAMES,
                        name="Games",
                    ),
                    SidebarItem(
                        icon=ft.Icons.PLAY_ARROW,
                        name="Play",
                    ),
                    SidebarItem(
                        icon=ft.Icons.STOP,
                        name="Stop",
                    ),
                    SidebarItem(
                        icon=ft.Icons.PAUSE,
                        name="Pause",
                    ),
                    SidebarItem(
                        icon=ft.Icons.REPLAY,
                        name="Replay",
                    ),
                    SidebarItem(
                        icon=ft.Icons.PLAY_ARROW,
                        name="Play",
                    ),
                ],
            ),
            SidebarGroup(
                title="Settings",
                items=[
                    SidebarItem(
                        icon=ft.Icons.SETTINGS,
                        name="Settings",
                    ),
                    SidebarItem(
                        icon=ft.Icons.PERSON,
                        name="Profile",
                    ),
                ],
            ),
        ]
    )
    page.add(
        Sidebar(
            sidebar_content=sidebar_content,
            company_name="Jumpingkids",
        )
    )


ft.app(target=main, port=9000)
