import flet as ft


class SubscriptionDialog(ft.AlertDialog):
    def __init__(self, on_select):
        self.on_select = on_select
        self.free_btn = ft.ElevatedButton(
            "Suscripción Gratuita",
            icon=ft.icons.LOCK_OPEN,
            on_click=lambda e: self._handle_select("free"),
            style=ft.ButtonStyle(
                bgcolor="#2D2242",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=8),
            )
        )
        self.premium_btn = ft.FilledButton(
            "Suscripción Premium",
            icon=ft.icons.STAR,
            on_click=lambda e: self._handle_select("premium"),
            style=ft.ButtonStyle(
                bgcolor="#2D2242",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=8),
            )
        )
        super().__init__(
            modal=True,
            title=ft.Text("Elige un tipo de suscripción"),
            content=ft.Column([
                ft.Text("Selecciona el tipo de suscripción para tus hijos."),
                self.free_btn,
                self.premium_btn
            ], tight=True),
            actions=[]
        )

    def _handle_select(self, subscription_type):
        self.open = False
        self.on_select(subscription_type)
