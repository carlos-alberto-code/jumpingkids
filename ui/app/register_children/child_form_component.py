import flet as ft

class ChildFormComponent(ft.Container):
    def __init__(self, on_save, on_cancel, index=0, initial_data=None):
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.index = index
        self.initial_data = initial_data or {}
        
        # Agregar un campo para la edad
        self.name_field = ft.TextField(
            label="Nombre completo",
            value=self.initial_data.get("full_name", ""),
            border_radius=8,
            filled=True,
            bgcolor=ft.colors.with_opacity(0.1, "purple200"),
            prefix_icon=ft.icons.PERSON,
            helper_text="Nombre y apellidos del niño",
            expand=True
        )
        
        self.age_field = ft.TextField(
            label="Edad",
            value=self.initial_data.get("age", ""),
            border_radius=8,
            keyboard_type=ft.KeyboardType.NUMBER,
            filled=True,
            bgcolor=ft.colors.with_opacity(0.1, "purple200"),
            prefix_icon=ft.icons.CAKE,
            helper_text="Entre 10-15 años",
            width=100
        )
        
        self.username_field = ft.TextField(
            label="Nombre de usuario",
            value=self.initial_data.get("username", ""),
            border_radius=8,
            filled=True,
            bgcolor=ft.colors.with_opacity(0.1, "purple200"),
            prefix_icon=ft.icons.ALTERNATE_EMAIL,
            helper_text="Para iniciar sesión",
            expand=True
        )
        
        self.password_field = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            value=self.initial_data.get("password", ""),
            border_radius=8,
            filled=True,
            bgcolor=ft.colors.with_opacity(0.1, "purple200"),
            prefix_icon=ft.icons.LOCK,
            helper_text="Fácil de recordar",
            expand=True
        )
        
        # Botones con estilos mejorados
        self.save_btn = ft.FilledButton(
            "Guardar",
            icon=ft.icons.SAVE,
            on_click=self._handle_save,
            style=ft.ButtonStyle(
                bgcolor="#7C4DFF",
                color="white",
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )
        
        self.cancel_btn = ft.OutlinedButton(
            "Cancelar",
            icon=ft.icons.CANCEL,
            on_click=self._handle_cancel,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.TRANSPARENT,
                color="#7C4DFF",
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                shape=ft.RoundedRectangleBorder(radius=8),
                side=ft.BorderSide(width=2, color="#7C4DFF"),
            ),
        )
        
        # Error message placeholder
        self.error_text = ft.Text(
            "",
            color="red600",
            size=12,
            visible=False
        )

        # Layout con diseño más estructurado
        super().__init__(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        # Encabezado
                        ft.Row(
                            [ft.Icon(ft.icons.CHILD_CARE, color="#7C4DFF"), 
                             ft.Text(
                                 f"Formulario de niño #{self.index+1}",
                                 weight=ft.FontWeight.BOLD,
                                 color="#7C4DFF",
                                 size=18
                             )],
                            spacing=5,
                        ),
                        ft.Divider(height=1, color="purple200"),
                        
                        # Campos de entrada
                        ft.Row(
                            [self.name_field, self.age_field],
                            spacing=10
                        ),
                        ft.Row(
                            [self.username_field],
                            spacing=10
                        ),
                        ft.Row(
                            [self.password_field],
                            spacing=10
                        ),
                        
                        # Mensaje de error
                        self.error_text,
                        
                        # Botones
                        ft.Row(
                            [
                                ft.Container(expand=True),  # Espaciador
                                self.cancel_btn,
                                self.save_btn,
                            ],
                            alignment=ft.MainAxisAlignment.END,
                            spacing=8
                        )
                    ], 
                    spacing=15,
                    tight=True),
                    padding=20,
                ),
                elevation=3,
                surface_tint_color="#F3E5F5",
                color="white",
                margin=10,
                border_radius=16,
            )
        )

    def _handle_save(self, e):
        # Validar datos
        name = self.name_field.value.strip()
        age = self.age_field.value.strip()
        username = self.username_field.value.strip()
        password = self.password_field.value.strip()
        
        # Verificar campos obligatorios
        if not name or not username or not password:
            self.show_error("Todos los campos son obligatorios")
            return
            
        # Validar edad
        if age:
            try:
                age_num = int(age)
                if age_num < 10 or age_num > 15:
                    self.show_error("La edad debe estar entre 10 y 15 años")
                    return
            except ValueError:
                self.show_error("La edad debe ser un número")
                return
        
        # Validar longitud de contraseña
        if len(password) < 6:
            self.show_error("La contraseña debe tener al menos 6 caracteres")
            return
            
        # Recopilar datos
        data = {
            "full_name": name,
            "age": age,
            "username": username,
            "password": password,
        }
        
        # Llamar al callback de guardado
        self.on_save(self.index, data)

    def _handle_cancel(self, e):
        self.on_cancel(self.index)
        
    def show_error(self, message):
        """Muestra un mensaje de error en el formulario"""
        self.error_text.value = message
        self.error_text.visible = True
        self.update()
        
        # Ocultar el mensaje después de 3 segundos
        def hide_error():
            self.error_text.visible = False
            self.update()
            
        if hasattr(self, "page") and self.page:
            self.page.timer_callback(3, hide_error)