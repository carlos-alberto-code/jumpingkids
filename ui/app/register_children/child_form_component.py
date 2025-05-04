import flet as ft

class ChildFormComponent(ft.Container):
    def __init__(self, on_save, on_cancel, index=0, initial_data=None):
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.index = index
        self.initial_data = initial_data or {}

        self.name_field = ft.TextField(label="Nombre completo", value=self.initial_data.get("full_name", ""))
        self.username_field = ft.TextField(label="Usuario", value=self.initial_data.get("username", ""))
        self.password_field = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, value=self.initial_data.get("password", ""))

        self.save_btn = ft.ElevatedButton("Guardar", on_click=self._handle_save, icon=ft.icons.SAVE)
        self.cancel_btn = ft.TextButton("Cancelar", on_click=self._handle_cancel, icon=ft.icons.CANCEL)

        super().__init__(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"Registro de niño #{self.index+1}", weight=ft.FontWeight.BOLD),
                        self.name_field,
                        self.username_field,
                        self.password_field,
                        ft.Row([
                            self.save_btn,
                            self.cancel_btn
                        ], alignment=ft.MainAxisAlignment.END)
                    ], tight=True),
                    padding=20,
                    width=400,
                ),
                elevation=2,
                margin=10
            )
        )

    def _handle_save(self, e):
        data = {
            "full_name": self.name_field.value.strip(),
            "username": self.username_field.value.strip(),
            "password": self.password_field.value.strip(),
        }
        self.on_save(self.index, data)

    def _handle_cancel(self, e):
        self.on_cancel(self.index)
