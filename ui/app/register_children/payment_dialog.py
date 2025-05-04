import flet as ft

class PaymentDialog(ft.AlertDialog):
    def __init__(self, on_success):
        self.on_success = on_success
        self.card_field = ft.TextField(label="Número de tarjeta", keyboard_type=ft.KeyboardType.NUMBER)
        self.pay_btn = ft.FilledButton(
            "Procesar pago",
            icon=ft.icons.PAYMENTS,
            on_click=self._handle_pay
        )
        super().__init__(
            modal=True,
            title=ft.Text("Pago de suscripción premium"),
            content=ft.Column([
                ft.Text("Ingresa los datos de tu tarjeta para completar el pago (demo)."),
                self.card_field,
                self.pay_btn
            ], tight=True),
            actions=[]
        )

    def _handle_pay(self, e):
        # Mock: cualquier valor es válido
        self.open = False
        self.on_success({"card_number": self.card_field.value})
