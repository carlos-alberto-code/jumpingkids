import flet as ft
import threading

class ChildFormComponent(ft.Container):
    def __init__(self, on_save, on_cancel, index=0, initial_data=None):
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.index = index
        self.initial_data = initial_data or {}

        # Campos de entrada con mayor tamaño y claridad visual
        self.name_field = ft.TextField(
            label="Nombre completo",
            value=self.initial_data.get("full_name", ""),
            border_radius=12,
            filled=True,
            bgcolor="#F8F0FF",
            prefix_icon=ft.icons.PERSON,
            helper_text="Nombre y apellidos del niño",
            expand=True,
            height=56,
            border_color="#7C4DFF",
            border_width=2,
            text_size=18,
        )
        self.age_field = ft.TextField(
            label="Edad",
            value=self.initial_data.get("age", ""),
            border_radius=12,
            keyboard_type=ft.KeyboardType.NUMBER,
            filled=True,
            bgcolor="#F8F0FF",
            prefix_icon=ft.icons.CAKE,
            helper_text="Entre 10-15 años",
            width=120,
            height=56,
            border_color="#7C4DFF",
            border_width=2,
            text_size=18,
        )
        self.username_field = ft.TextField(
            label="Nombre de usuario",
            value=self.initial_data.get("username", ""),
            border_radius=12,
            filled=True,
            bgcolor="#F8F0FF",
            prefix_icon=ft.icons.ALTERNATE_EMAIL,
            helper_text="Para iniciar sesión",
            expand=True,
            height=56,
            border_color="#7C4DFF",
            border_width=2,
            text_size=18,
        )
        self.password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            value=self.initial_data.get("password", ""),
            border_radius=12,
            filled=True,
            bgcolor="#F8F0FF",
            prefix_icon=ft.icons.LOCK,
            helper_text="Fácil de recordar",
            expand=True,
            height=56,
            border_color="#7C4DFF",
            border_width=2,
            text_size=18,
        )

        # Botones grandes y notorios
        self.save_btn = ft.FilledButton(
            "Guardar",
            icon=ft.icons.SAVE,
            on_click=self._handle_save,
            style=ft.ButtonStyle(
                bgcolor="#7C4DFF",
                color="white",
                padding=ft.padding.symmetric(horizontal=30, vertical=16),
                shape=ft.RoundedRectangleBorder(radius=10),
                text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD),
            ),
            height=48,
            width=160,
        )
        self.cancel_btn = ft.OutlinedButton(
            "Cancelar",
            icon=ft.icons.CANCEL,
            on_click=self._handle_cancel,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.TRANSPARENT,
                color="#7C4DFF",
                padding=ft.padding.symmetric(horizontal=30, vertical=16),
                shape=ft.RoundedRectangleBorder(radius=10),
                side=ft.BorderSide(width=2, color="#7C4DFF"),
                text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD),
            ),
            height=48,
            width=160,
        )

        self.error_text = ft.Text(
            "",
            color="red600",
            size=14,
            visible=False,
            weight=ft.FontWeight.BOLD,
        )

        # Layout principal mejorado
        super().__init__(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.icons.CHILD_CARE, color="#7C4DFF", size=28),
                            ft.Text(
                                f"Formulario de niño #{self.index+1}",
                                weight=ft.FontWeight.BOLD,
                                color="#7C4DFF",
                                size=22,
                            )
                        ], spacing=8),
                        ft.Divider(height=2, color="#7C4DFF"),
                        ft.Row([
                            self.name_field,
                            self.age_field
                        ], spacing=16),
                        self.username_field,
                        self.password_field,
                        self.error_text,
                        ft.Row([
                            self.cancel_btn,
                            self.save_btn
                        ], alignment=ft.MainAxisAlignment.END, spacing=16),
                    ],
                    spacing=18,
                    tight=True),
                    padding=ft.padding.symmetric(horizontal=32, vertical=32),
                    width=420,
                ),
                elevation=6,
                surface_tint_color="#F3E5F5",
                color="white",
                margin=ft.margin.only(top=10, bottom=10),
                shadow_color="#E0E0E0",
            ),
            alignment=ft.alignment.center,
            border_radius=18,
            bgcolor="#F3E5F5",
            shadow=ft.BoxShadow(blur_radius=16, color="#E0E0E0"),
        )

    def _handle_save(self, e):
        name = self.name_field.value.strip()
        age = self.age_field.value.strip()
        username = self.username_field.value.strip()
        password = self.password_field.value.strip()
        if not name or not username or not password:
            self.show_error("Todos los campos son obligatorios")
            return
        if age:
            try:
                age_num = int(age)
                if age_num < 10 or age_num > 15:
                    self.show_error("La edad debe estar entre 10 y 15 años")
                    return
            except ValueError:
                self.show_error("La edad debe ser un número")
                return
        if len(password) < 6:
            self.show_error("La contraseña debe tener al menos 6 caracteres")
            return
        data = {
            "full_name": name,
            "age": age,
            "username": username,
            "password": password,
        }
        self.on_save(self.index, data)

    def _handle_cancel(self, e):
        self.on_cancel(self.index)

    def show_error(self, message):
        self.error_text.value = message
        self.error_text.visible = True
        self.update()
        def hide_error():
            self.error_text.visible = False
            self.update()
        # Usar threading.Timer para ocultar el mensaje después de 3 segundos
        threading.Timer(3, hide_error).start()