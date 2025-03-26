import flet as ft


class JumpingKidsAppbar(ft.AppBar):

    def __init__(self, title: str, username: str) -> None:
        super().__init__(
            title=ft.Text(title),
            center_title=True,
            automatically_imply_leading=False,
            elevation=5,
            actions=[
                ft.Text(username),
                ft.VerticalDivider(visible=False),
                ft.PopupMenuButton(
                    tooltip="Usuario",
                    icon=ft.Icons.ACCOUNT_CIRCLE,
                    elevation=5,
                    items=[
                        ft.PopupMenuItem(
                            text="Perfil",
                            icon=ft.Icons.PERSON,
                        ),
                        ft.PopupMenuItem(
                            text="Configuración",
                            icon=ft.Icons.SETTINGS,
                        ),
                        ft.PopupMenuItem(
                            text="Cerrar sesión",
                            icon=ft.Icons.LOGOUT,
                        ),
                    ],
                ),
                ft.Container(width=15)
            ]
        )