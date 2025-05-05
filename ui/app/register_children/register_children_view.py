import flet as ft
from ui.app.register_children.child_form_component import ChildFormComponent
from ui.app.register_children.child_list_component import ChildListComponent
from ui.app.register_children.animation_panel import AnimationPanel

MAX_CHILDREN = 3

class RegisterChildrenView(ft.View):
    def __init__(self, on_finish, registration_service):
        self._registration_service = registration_service
        self._on_finish = on_finish
        self._children_data = []
        self._active_forms = []  # indices de active forms
        self._next_index = 0

        # Componentes principales
        self._animation_panel = AnimationPanel()
        self._child_list = ChildListComponent(self._children_data)
        
        # Botones de acción
        self._add_child_btn = ft.FilledButton(
            "Agregar hijo",
            icon=ft.icons.PERSON_ADD,
            on_click=self._handle_add_child,
            style=ft.ButtonStyle(
                bgcolor="#2D2242",
                color="white",
                shape=ft.RoundedRectangleBorder(radius=8),
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
            )
        )

        # Diálogo para el formulario de registro de niño
        self._child_form_dialog = ft.AlertDialog(
            modal=True,
            content=None,  # Se asigna dinámicamente
            actions=[],
            on_dismiss=lambda e: self._handle_cancel_form_dialog(),
        )
        
        self._finish_btn = ft.FilledButton(
            "Finalizar registro",
            icon=ft.icons.CHECK_CIRCLE,
            on_click=self._handle_finish,
            disabled=True,
            style=ft.ButtonStyle(
                bgcolor="#2D2242",
                color="white",
                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                shape=ft.RoundedRectangleBorder(radius=8),
            )
        )
        
        # Layout principal
        super().__init__(
            route="/register-child",
            padding=0,
            controls=[
                ft.ResponsiveRow(
                    [
                        # Panel de animación (visible solo en pantallas grandes)
                        ft.Column(
                            [self._animation_panel],
                            col={"md": 5, "sm": 0},  # Oculto en móviles
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        
                        # Panel principal
                        ft.Column(
                            [
                                # Encabezado
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Registro de hijos", 
                                                size=28, 
                                                weight=ft.FontWeight.BOLD, 
                                                color="#7C4DFF"
                                            ),
                                            ft.Text(
                                                f"Agrega hasta {MAX_CHILDREN} niños para comenzar.",
                                                size=16, 
                                                color="grey700",
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    padding=ft.padding.only(top=30, bottom=20),
                                ),
                                
                                # Contenedor para niños registrados
                                ft.Container(
                                    ft.Column(
                                        [
                                            ft.Text(
                                                "Niños registrados", 
                                                size=18, 
                                                weight=ft.FontWeight.BOLD,
                                                color="#7C4DFF",
                                            ),
                                            self._child_list,
                                        ],
                                    ),
                                    padding=10,
                                    border_radius=10,
                                    bgcolor="#F8F0FF",  # Color de fondo más claro
                                    visible=True,
                                    margin=ft.margin.only(bottom=20),
                                ),
                                
                                # Botón para agregar hijo
                                ft.Container(
                                    self._add_child_btn,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(bottom=20),
                                ),
                                
                                # Botón para finalizar
                                ft.Container(
                                    self._finish_btn,
                                    alignment=ft.alignment.center,
                                    margin=ft.margin.only(bottom=30),
                                ),
                            ],
                            col={"md": 7, "sm": 12},
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    expand=True,
                )
            ],
            bgcolor=ft.Colors.GREY_100,
        )

    def _handle_add_child(self, e):
        # Verificar si ya se alcanzó el límite de niños
        total = len(self._children_data)
        if total >= MAX_CHILDREN:
            # Mostrar mensaje de límite alcanzado
            if hasattr(self, "page") and self.page:
                self.page.open(ft.SnackBar(
                    content=ft.Text(f"Has alcanzado el límite de {MAX_CHILDREN} niños."),
                    bgcolor="#7C4DFF",
                    action="Entendido"
                ))
                self.page.update()
            return
        # Crear formulario y mostrar en diálogo
        idx = self._next_index
        form = ChildFormComponent(
            on_save=self._handle_save_child,
            on_cancel=self._handle_cancel_form,
            index=idx
        )
        self._child_form_dialog.content = form
        self._child_form_dialog.actions = []
        self._active_form_index = idx
        if hasattr(self, "page") and self.page:
            self.page.open(self._child_form_dialog)
            self.page.update()
        self._next_index += 1

    def _handle_save_child(self, index, data):
        # Guardar datos del niño
        self._children_data.append(data)
        self._registration_service.add_child(data)
        # Actualizar lista de niños
        self._child_list.children_data = self._children_data
        self._child_list.update()
        # Cerrar el diálogo
        if hasattr(self, "page") and self.page:
            self.page.close(self._child_form_dialog)
            self.page.update()
        # Actualizar botones
        self._update_buttons()
        # Mostrar mensaje de éxito
        if hasattr(self, "page") and self.page:
            self.page.open(ft.SnackBar(
                content=ft.Text(f"¡{data['full_name']} ha sido registrado con éxito!"),
                bgcolor="green",
                action="¡Genial!"
            ))
            self.page.update()

    def _handle_cancel_form(self, index=None):
        # Cerrar el diálogo si está abierto
        if hasattr(self, "page") and self.page:
            self.page.close(self._child_form_dialog)
            self.page.update()
        # Actualizar botones
        self._update_buttons()
        self.update()

    def _handle_cancel_form_dialog(self):
        # Callback para on_dismiss del diálogo
        self._handle_cancel_form()

    def _handle_finish(self, e):
        # Verificar si hay formularios activos
        if len(self._active_forms) > 0:
            # Mostrar mensaje de advertencia
            self._dialog = ft.AlertDialog(
                title=ft.Text("Formularios sin guardar"),
                content=ft.Text(
                    "Hay formularios que no has guardado. "
                    "¿Quieres guardarlos antes de continuar?"
                ),
                actions=[
                    ft.TextButton("Ignorar", on_click=lambda _: self._confirm_finish(e)),
                    ft.FilledButton(
                        "Guardar primero", 
                        on_click=lambda _: self.page.close(self._dialog) if self.page else None
                    ),
                ],
            )
            if hasattr(self, "page") and self.page:
                self.page.open(self._dialog)
                self.page.update()
        else:
            self._confirm_finish(e)

    def _confirm_finish(self, e):
        # Cerrar diálogo si está abierto
        if hasattr(self, "page") and self.page and hasattr(self, "_dialog"):
            self.page.close(self._dialog)
            self.page.update()
        # Verificar si hay niños registrados
        if len(self._children_data) == 0:
            # Mostrar mensaje de advertencia
            self._dialog = ft.AlertDialog(
                title=ft.Text("Sin niños registrados"),
                content=ft.Text(
                    "No has registrado ningún niño. "
                    "¿Estás seguro de que quieres continuar?"
                ),
                actions=[
                    ft.TextButton("Cancelar", on_click=lambda _: self.page.close(self._dialog)),
                    ft.FilledButton(
                        "Continuar sin niños", 
                        on_click=lambda _: self._finish_registration()
                    ),
                ],
            )
            if hasattr(self, "page") and self.page:
                self.page.open(self._dialog)
                self.page.update()
        else:
            self._finish_registration()

    def _finish_registration(self):
        # Cerrar diálogo si está abierto
        if hasattr(self, "page") and self.page and hasattr(self, "_dialog"):
            self.page.close(self._dialog)
            self.page.update()
        # Llamar al callback de finalización
        self._on_finish(self._children_data)

    def _update_buttons(self):
        # Actualizar estado del botón de agregar
        total = len(self._children_data)
        self._add_child_btn.disabled = (total >= MAX_CHILDREN)
        
        # Actualizar estado del botón de finalizar
        self._finish_btn.disabled = (len(self._children_data) == 0)

    @property
    def children_data(self):
        return self._children_data
    