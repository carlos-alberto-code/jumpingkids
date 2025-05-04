import flet as ft

class ChildListComponent(ft.Container):
    def __init__(self, children_data=None):
        self.children_data = children_data or []
        self.title = ft.Text("Niños registrados:", weight=ft.FontWeight.BOLD)
        self.list_column = ft.Column([
            ft.ListTile(
                title=ft.Text(child["full_name"]),
                subtitle=ft.Text(child["username"]),
                leading=ft.Icon(ft.icons.CHILD_CARE),
            ) for child in self.children_data
        ], tight=True)
        super().__init__(
            content=ft.Column([
                self.title,
                self.list_column if self.children_data else ft.Text("No hay niños registrados aún.", italic=True, color=ft.colors.GREY)
            ], tight=True)
        )

    def update(self):
        self.list_column.controls.clear()
        for child in self.children_data:
            self.list_column.controls.append(
                ft.ListTile(
                    title=ft.Text(child["full_name"]),
                    subtitle=ft.Text(child["username"]),
                    leading=ft.Icon(ft.icons.CHILD_CARE),
                )
            )
        super().update()
