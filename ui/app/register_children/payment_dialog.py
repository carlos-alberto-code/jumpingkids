import flet as ft

class PaymentDialog(ft.AlertDialog):
    def __init__(self, on_success):
        self.on_success = on_success
        self.card_field = ft.TextField(label="Número de tarjeta", keyboard_type=ft.KeyboardType.NUMBER, bgcolor=ft.Colors.GREY_100)
        super().__init__(
            modal=True,
            title=ft.Text("Pago de suscripción premium"),
            content=ft.Column([
                ft.Text("Ingresa los datos de tu tarjeta para completar el pago (demo)."),
                self.card_field
            ], tight=True),
            actions=[
                ft.TextButton(
                    "Procesar pago",
                    icon=ft.icons.PAYMENTS,
                    on_click=self._handle_pay,
                    style=ft.ButtonStyle(
                        bgcolor="#2D2242",
                        color="white",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    )
                )
            ]
        )

    def _handle_pay(self, e):
        # Mock: cualquier valor es válido
        if self.on_success:
            self.on_success({"card_number": self.card_field.value})
