import flet as ft
from domain.model import Exercise
from ui.app.child_free_app.components.exercise_view.exercise_card import ExerciseCard

class ExerciseListComponent(ft.Container):
    """Componente que muestra la lista de ejercicios con filtros por categoría."""
    
    def __init__(self, exercises=None, on_exercise_selected=None):
        """
        Inicializa el componente de lista de ejercicios.
        
        Args:
            exercises (list): Lista de objetos Exercise a mostrar
            on_exercise_selected (callable): Función a ejecutar cuando se selecciona un ejercicio
        """
        self.exercises = exercises or []
        self.on_exercise_selected = on_exercise_selected or (lambda exercise: None)
        self.filtered_exercises = self.exercises.copy()
        self.selected_category = "Todos"
        
        # Categorías para filtrar
        self.categories = ["Todos", "Resistencia", "Fuerza", "Elasticidad", "Cardio"]
        
        # Crear contenido del componente
        content = ft.Column([
            ft.Row([
                ft.Text("Ejercicios disponibles", size=24, weight=ft.FontWeight.BOLD, color="green700"),
                ft.Container(
                    content=ft.Text("¡NUEVO!", color="white", size=10, weight=ft.FontWeight.BOLD),
                    bgcolor="orange400",
                    border_radius=15,
                    padding=ft.padding.symmetric(horizontal=12, vertical=4),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(left=10)
                )
            ]),
            
            # Filtros de categoría
            ft.Container(
                margin=ft.margin.only(top=5, bottom=10),
                content=ft.Row(
                    [self._create_category_filter(cat) for cat in self.categories],
                    scroll=ft.ScrollMode.AUTO
                )
            ),
            
            # ListView con altura específica y scroll para los ejercicios
            ft.Container(
                height=400,
                content=ft.ListView(
                    [
                        self._create_exercise_card(exercise) for exercise in self.filtered_exercises
                    ],
                    spacing=10,
                    padding=ft.padding.symmetric(vertical=10),
                    auto_scroll=True
                ),
                border_radius=8,
                border=ft.border.all(1, "green100"),
            )
        ], spacing=10)
        
        # Inicializar el contenedor con los estilos adecuados
        super().__init__(
            content=content,
            expand=2
        )
    
    def _create_category_filter(self, category):
        """
        Crea un filtro de categoría clickeable.
        
        Args:
            category (str): Nombre de la categoría
        
        Returns:
            ft.Container: Contenedor del filtro de categoría
        """
        is_selected = category == self.selected_category
        
        return ft.Container(
            content=ft.Text(category, size=12, color="green800"),
            bgcolor="green50" if is_selected else "white",
            border=ft.border.all(1, "green200"),
            border_radius=15,
            padding=ft.padding.symmetric(horizontal=15, vertical=5),
            margin=ft.margin.only(right=5),
            on_click=lambda e, cat=category: self._apply_category_filter(cat)
        )
    
    def _create_exercise_card(self, exercise):
        """
        Crea una tarjeta de ejercicio.
        
        Args:
            exercise (Exercise): Objeto Exercise a mostrar
        
        Returns:
            ExerciseCard: Componente de tarjeta de ejercicio
        """
        return ExerciseCard(
            exercise=exercise,
            on_click=lambda e, ex=exercise: self._handle_exercise_selected(ex)
        )
    
    def _handle_exercise_selected(self, exercise):
        """
        Maneja la selección de un ejercicio.
        
        Args:
            exercise (Exercise): Ejercicio seleccionado
        """
        if self.on_exercise_selected:
            self.on_exercise_selected(exercise)
    
    def _apply_category_filter(self, category):
        """
        Aplica un filtro de categoría a la lista de ejercicios.
        
        Args:
            category (str): Categoría para filtrar
        """
        self.selected_category = category
        
        # Filtrar ejercicios por categoría
        if category == "Todos":
            self.filtered_exercises = self.exercises.copy()
        else:
            self.filtered_exercises = [ex for ex in self.exercises if ex.category == category]
        
        # Actualizar los botones de filtro
        category_row = self.content.controls[1].content
        for i, cat_container in enumerate(category_row.controls):
            cat_text = cat_container.content.value
            cat_container.bgcolor = "green50" if cat_text == category else "white"
        
        # Actualizar la lista de ejercicios
        exercise_list = self.content.controls[2].content
        exercise_list.controls = [self._create_exercise_card(ex) for ex in self.filtered_exercises]
        
        self.update()
    
    def set_exercises(self, exercises):
        """
        Actualiza la lista de ejercicios.
        
        Args:
            exercises (list): Nueva lista de objetos Exercise
        """
        self.exercises = exercises
        self._apply_category_filter(self.selected_category)
    
    def set_on_exercise_selected(self, callback):
        """
        Actualiza el callback para la selección de ejercicios.
        
        Args:
            callback (callable): Nuevo callback
        """
        self.on_exercise_selected = callback or (lambda exercise: None)