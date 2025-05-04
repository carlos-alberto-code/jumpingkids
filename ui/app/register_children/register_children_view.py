import flet as ft
from ui.app.register_children.child_form_component import ChildFormComponent
from ui.app.register_children.child_list_component import ChildListComponent

MAX_CHILDREN = 3

class RegisterChildrenView(ft.View):
    def __init__(self, on_finish, registration_service):
        self._registration_service = registration_service
        self._on_finish = on_finish
        self._children_data = []
        self._active_forms = []  # indices of active forms
        self._next_index = 0

        self._form_column = ft.Column([], scroll=ft.ScrollMode.ALWAYS)
        self._child_list = ChildListComponent(self._children_data)
        self._add_child_btn = ft.ElevatedButton(
            "Agregar hijo",
            icon=ft.icons.ADD,
            on_click=self._handle_add_child,
            disabled=False
        )
        self._finish_btn = ft.FilledButton(
            "Finalizar registro",
            icon=ft.icons.CHECK,
            on_click=self._handle_finish,
            disabled=True
        )

        super().__init__(
            route="/register-child",
            padding=30,
            controls=[
                ft.Column([
                    ft.Text("Registro de hijos", size=22, weight=ft.FontWeight.BOLD),
                    ft.Text("Agrega hasta 3 niños. Guarda cada formulario para agregarlos a la lista."),
                    self._add_child_btn,
                    ft.Divider(),
                    ft.Row([
                        self._form_column,
                        ft.VerticalDivider(),
                        self._child_list,
                    ], alignment=ft.MainAxisAlignment.START),
                    self._finish_btn
                ], tight=True)
            ],
        )

    def _handle_add_child(self, e):
        if len(self._active_forms) + len(self._children_data) < MAX_CHILDREN:
            idx = self._next_index
            form = ChildFormComponent(
                on_save=self._handle_save_child,
                on_cancel=self._handle_cancel_form,
                index=idx
            )
            self._form_column.controls.append(form)
            self._active_forms.append((idx, form))
            self._next_index += 1
            self._update_buttons()
            self.update()

    def _handle_save_child(self, index, data):
        self._children_data.append(data)
        # Remover el formulario de la columna
        for i, (idx, form) in enumerate(self._active_forms):
            if idx == index:
                self._form_column.controls.remove(form)
                self._active_forms.pop(i)
                break
        self._registration_service.add_child(data)
        self._child_list.children_data = self._children_data
        self._child_list.update()
        self._update_buttons()
        self.update()

    def _handle_cancel_form(self, index):
        for i, (idx, form) in enumerate(self._active_forms):
            if idx == index:
                self._form_column.controls.remove(form)
                self._active_forms.pop(i)
                break
        self._update_buttons()
        self.update()

    def _handle_finish(self, e):
        self._on_finish(self._children_data)

    def _update_buttons(self):
        self._add_child_btn.disabled = (len(self._active_forms) + len(self._children_data) >= MAX_CHILDREN)
        self._finish_btn.disabled = (len(self._children_data) == 0)

    @property
    def children_data(self):
        return self._children_data
