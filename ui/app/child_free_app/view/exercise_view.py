import flet as ft

from ui.app.components.appbar import JumpingKidsAppbar
from ui.app.components.sidebar import Sidebar


class Searcher(ft.TextField):
    def __init__(self, on_submit=None, on_change=None):
        self._on_change = on_change
        self._on_submit = on_submit
        super().__init__(
            label="Buscar ejercicio",
            prefix_icon=ft.icons.SEARCH,
            border_radius=10,
            height=40,
            label_style=ft.TextStyle(
                size=13,
            ),
            text_style=ft.TextStyle(
                size=13,
            ),
            expand=True,
            on_submit=self._on_submit,
            on_change=self._on_change,
        )



class ExerciseFilter(ft.PopupMenuButton):
    def __init__(self, icon: ft.Icons, items: list[ft.PopupMenuItem]):
        super().__init__(
            icon=icon,
            items=items,
        )


class ExerciseFilterBar(ft.Row):
    def __init__(self, searcher: Searcher, filter: ft.PopupMenuButton):
        super().__init__(
            controls=[
                searcher,
                filter,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )



class ExerciseLayout(ft.Container):

    def __init__(
        self,
        sidebar: Sidebar,
        exercise_bar: ExerciseFilterBar,
        exercise_list: ft.GridView | ft.ListView,
        exercise_panel: ft.Column,
    ) -> None:
        
        left_content = sidebar

        center_content = ft.Column(
            controls=[
                exercise_bar,
                exercise_list,
            ]
        )

        right_content = exercise_panel
        super().__init__(
            content=ft.Row(
                controls=[
                    left_content,
                    center_content,
                    right_content,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                expand=True,
            ),
            padding=0,
        )


class ExerciseView(ft.View):
    def __init__(
        self,
        on_submit=None,
        on_filter_by_category=None,
        on_filter_by_level=None,
        on_view_exercise_details=None,
        on_favorite_exercise_click=None,
    ) -> None:
        
        # Eventos
        self._on_submit = on_submit
        self._on_filter_by_level = on_filter_by_level
        self._on_filter_by_category = on_filter_by_category
        self._on_view_exercise_details = on_view_exercise_details
        self._on_favorite_exercise_click = on_favorite_exercise_click

        # Componentes
        self._sidebar = Sidebar()
        self._layout = ExerciseLayout()
        super().__init__(
            route="/ejercicios",
            appbar=JumpingKidsAppbar(
                title="Ejercicios",
                username="Usuario",
            ),
            padding=0,
            controls=[self._layout]
        )
    
    @property
    def on_submit(self):
        return self._on_submit
    
    @on_submit.setter
    def on_submit(self, value):
        self._on_submit = value
    
    @property
    def on_filter_by_level(self):
        return self._on_filter_by_level
    
    @on_filter_by_level.setter
    def on_filter_by_level(self, value):
        self._on_filter_by_level = value

    @property
    def on_filter_by_category(self):
        return self._on_filter_by_category
    
    @on_filter_by_category.setter
    def on_filter_by_category(self, value):
        self._on_filter_by_category = value
    
    @property
    def on_view_exercise_details(self):
        return self._on_view_exercise_details
    
    @on_view_exercise_details.setter
    def on_view_exercise_details(self, value):
        self._on_view_exercise_details = value

    @property
    def on_favorite_exercise_click(self):
        return self._on_favorite_exercise_click
    
    @on_favorite_exercise_click.setter
    def on_favorite_exercise_click(self, value):
        self._on_favorite_exercise_click = value
