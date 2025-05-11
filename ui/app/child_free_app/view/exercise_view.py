import flet as ft

from ui.app.components.sidebar import Sidebar
from ui.app.components.appbar import JumpingKidsAppbar
from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO
from ui.app.child_free_app.components.exercise_view.exercise_list_component import ExerciseList
from ui.app.child_free_app.components.exercise_view.exercise_player_component import ExercisePlayerComponent


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
    def __init__(self, searcher: Searcher, filter_by_category: ft.PopupMenuButton, filter_by_level: ft.PopupMenuButton):
        super().__init__(
            controls=[
                searcher,
                filter_by_category,
                filter_by_level,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )


class ExerciseDetailPanel(ft.Column):
    def __init__(self):
        self.title = ft.Text("Selecciona un ejercicio", size=20, weight=ft.FontWeight.BOLD)
        self.description = ft.Text("Haz clic en un ejercicio para ver los detalles", size=14)
        self.exercise_player = ExercisePlayerComponent()
        
        super().__init__(
            controls=[
                self.title,
                ft.Divider(),
                self.description,
                self.exercise_player
            ],
            spacing=10,
            expand=True,
        )
    
    def update_with_exercise(self, exercise: ExerciseDTO):
        self.title.value = exercise.name
        self.description.value = exercise.description
        self.exercise_player.set_exercise(exercise)
        self.update()


class ExerciseLayout(ft.Container):
    def __init__(
        self,
        sidebar: Sidebar,
        exercise_bar: ExerciseFilterBar,
        exercise_list: ExerciseList,
        exercise_panel: ExerciseDetailPanel,
    ) -> None:
        self._levels: list[LevelDTO] = []
        self._exercises: list[ExerciseDTO] = []
        self._categories: list[CategoryDTO] = []
        
        left_content = sidebar

        center_content = ft.Column(
            controls=[
                exercise_bar,
                exercise_list,
            ],
            expand=True,
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
            expand=True,
        )
    
    @property
    def exercises(self) -> list[ExerciseDTO]:
        return self._exercises
    
    @exercises.setter
    def exercises(self, values: list[ExerciseDTO]) -> None:
        self._exercises = values

    @property
    def categories(self) -> list[CategoryDTO]:
        return self._categories
    
    @categories.setter
    def categories(self, values: list[CategoryDTO]) -> None:
        self._categories = values
    
    @property
    def levels(self) -> list[LevelDTO]:
        return self._levels
    
    @levels.setter
    def levels(self, values: list[LevelDTO]) -> None:
        self._levels = values


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

        # Data
        self._levels: list[LevelDTO] = []
        self._exercises: list[ExerciseDTO] = []
        self._categories: list[CategoryDTO] = []

        # Componentes
        self._sidebar = Sidebar(title="JumpingKids", on_change=self._handle_sidebar_change)
        self._sidebar.keys = {
            "Ejercicios": ft.icons.FITNESS_CENTER,
            "Favoritos": ft.icons.FAVORITE,
            "Estadísticas": ft.icons.BAR_CHART,
            "Perfil": ft.icons.PERSON,
        }
        
        # Crear componentes para la vista
        self._searcher = Searcher(on_submit=self._on_submit)
        
        # Inicializar filtros vacíos (se poblarán cuando se tengan datos)
        self._filter_by_category = ExerciseFilter(
            icon=ft.Icons.CATEGORY,
            items=[]
        )
        
        self._filter_by_level = ExerciseFilter(
            icon=ft.Icons.EQUALIZER,
            items=[]
        )
        
        self._exercise_bar = ExerciseFilterBar(
            searcher=self._searcher,
            filter_by_category=self._filter_by_category,
            filter_by_level=self._filter_by_level
        )
        
        self._exercise_list = ExerciseList(
            exercises=[],
            on_exercise_select=self._on_view_exercise_details
        )
        
        self._exercise_panel = ExerciseDetailPanel()
        
        # Crear layout principal
        self._layout = ExerciseLayout(
            sidebar=self._sidebar,
            exercise_bar=self._exercise_bar,
            exercise_list=self._exercise_list,
            exercise_panel=self._exercise_panel
        )
        
        super().__init__(
            route="/ejercicios",
            appbar=JumpingKidsAppbar(
                title="Ejercicios",
                username="Usuario",
            ),
            padding=0,
            controls=[self._layout]
        )
    
    def _handle_sidebar_change(self, e):
        # Manejar cambios en la barra lateral
        pass
    
    @property
    def exercises(self) -> list[ExerciseDTO]:
        return self._exercises
    
    @exercises.setter
    def exercises(self, values: list[ExerciseDTO]) -> None:
        self._exercises = values
        self._layout.exercises = values
        self._exercise_list.exercises = values
        self._exercise_list.update()
        
    @property
    def categories(self) -> list[CategoryDTO]:
        return self._categories
    
    @categories.setter
    def categories(self, values: list[CategoryDTO] | None) -> None:
        if values is not None:
            self._categories = values
            self._layout.categories = values
            
            # Actualizar los items del filtro de categorías
            self._filter_by_category.items = [
                ft.PopupMenuItem(
                    text=category.name,
                    on_click=self._on_filter_by_category,
                    data=category
                ) for category in values
            ]
    
    @property
    def levels(self) -> list[LevelDTO]:
        return self._levels
    
    @levels.setter
    def levels(self, values: list[LevelDTO] | None) -> None:
        if values is not None:
            self._levels = values
            self._layout.levels = values
            
            # Actualizar los items del filtro de niveles
            self._filter_by_level.items = [
                ft.PopupMenuItem(
                    text=level.name,
                    on_click=self._on_filter_by_level,
                    data=level
                ) for level in values
            ]

    @property
    def on_submit(self):
        return self._on_submit
    
    @on_submit.setter
    def on_submit(self, value):
        self._on_submit = value
        self._searcher.on_submit = value
    
    @property
    def on_filter_by_level(self):
        return self._on_filter_by_level
    
    @on_filter_by_level.setter
    def on_filter_by_level(self, value):
        self._on_filter_by_level = value
        # Actualizar los items del filtro para usar el nuevo callback
        if self._levels:
            self._filter_by_level.items = [
                ft.PopupMenuItem(
                    text=level.name,
                    on_click=value,
                    data=level
                ) for level in self._levels
            ]

    @property
    def on_filter_by_category(self):
        return self._on_filter_by_category
    
    @on_filter_by_category.setter
    def on_filter_by_category(self, value):
        self._on_filter_by_category = value
        # Actualizar los items del filtro para usar el nuevo callback
        if self._categories:
            self._filter_by_category.items = [
                ft.PopupMenuItem(
                    text=category.name,
                    on_click=value,
                    data=category
                ) for category in self._categories
            ]
    
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

    def update_panel(self, exercise: ExerciseDTO) -> None:
        """Actualiza el panel de detalles con el ejercicio seleccionado"""
        self._exercise_panel.update_with_exercise(exercise)