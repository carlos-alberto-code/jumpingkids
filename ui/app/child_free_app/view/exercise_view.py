import flet as ft
from domain.model import Exercise, Category, Level, SubscriptionType
from ui.app.child_free_app.components.exercise_view import (
    ProgressComponent,
    ExerciseListComponent,
    ExercisePlayerComponent
)

class ExerciseView(ft.View):
    def __init__(self, appbar: ft.AppBar | None = None) -> None:
        # Instancias dummy para los modelos requeridos
        default_subscription = SubscriptionType(id=1, name="Free")
        fuerza_category = Category(id=1, name="Fuerza", routines=[], exercises=[])
        resistencia_category = Category(id=2, name="Resistencia", routines=[], exercises=[])
        elasticidad_category = Category(id=3, name="Elasticidad", routines=[], exercises=[])
        cardio_category = Category(id=4, name="Cardio", routines=[], exercises=[])
        nivel_1 = Level(id=1, name="Nivel 1", routines=[], exercises=[])
        nivel_2 = Level(id=2, name="Nivel 2", routines=[], exercises=[])

        # Lista de ejercicios de ejemplo congruente con el modelo de dominio
        ejercicios = [
            Exercise(id=1, name="Saltos estrella", description="Saltos abriendo brazos y piernas", level=nivel_1, category=resistencia_category, subscription_types=[default_subscription]),
            Exercise(id=2, name="Sentadillas básicas", description="Sentadillas para principiantes", level=nivel_1, category=fuerza_category, subscription_types=[default_subscription]),
            Exercise(id=3, name="Estiramiento de brazos", description="Estirar brazos en diferentes direcciones", level=nivel_1, category=elasticidad_category, subscription_types=[default_subscription]),
            Exercise(id=4, name="Flexiones de brazos", description="Flexiones para fortalecer el tren superior", level=nivel_2, category=fuerza_category, subscription_types=[default_subscription]),
            Exercise(id=5, name="Abdominales", description="Ejercicio para fortalecer el abdomen", level=nivel_2, category=fuerza_category, subscription_types=[default_subscription]),
            Exercise(id=6, name="Caminata rápida", description="Caminata a paso ligero para mejorar resistencia", level=nivel_1, category=cardio_category, subscription_types=[default_subscription]),
        ]
        
        # Crear componentes refactorizados
        self.progress_component = ProgressComponent(active_days=2, total_days=7)
        self.exercise_list_component = ExerciseListComponent(
            exercises=ejercicios,
            on_exercise_selected=self._on_exercise_selected
        )
        self.exercise_player_component = ExercisePlayerComponent(
            on_exercise_finished=self._on_exercise_finished,
            on_exercise_completed=self._on_exercise_completed
        )
        
        super().__init__(
            route="/ejercicios",
            appbar=appbar,
            controls=[
                ft.Container(
                    padding=20,
                    expand=True,
                    content=ft.Column([
                        # Barra de progreso semanal
                        self.progress_component,
                        
                        # Hacemos toda la columna principal scrolleable y expandible
                        ft.Column([
                            ft.Row(
                                spacing=20,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    # Contenedor para la lista de ejercicios
                                    self.exercise_list_component,
                                    
                                    # Contenedor para la visualización y ejecución de ejercicio
                                    self.exercise_player_component
                                ]
                            )
                        ], scroll=ft.ScrollMode.AUTO, expand=True)
                    ])
                )
            ]
        )
    
    def _on_exercise_selected(self, exercise: Exercise):
        """Método para manejar cuando se selecciona un ejercicio."""
        print(f"Ejercicio seleccionado: {exercise.name}")
        self.exercise_player_component.set_exercise(exercise)
    
    def _on_exercise_finished(self):
        """Método para manejar cuando termina el cronómetro."""
        print("¡Tiempo finalizado!")
    
    def _on_exercise_completed(self, e):
        """Método para manejar cuando se marca un ejercicio como completado."""
        if hasattr(self, "page") and self.page:
            self.page.open(ft.SnackBar(
                content=ft.Row([
                    ft.Icon(ft.icons.EMOJI_EVENTS, color="amber500"),
                    ft.Text("¡Muy bien! +10 puntos", color="white")
                ]),
                bgcolor="green700",
                action="¡Genial!"
            ))
            self.page.update()
