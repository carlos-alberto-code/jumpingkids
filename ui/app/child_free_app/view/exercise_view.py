import flet as ft
from domain.model import Exercise
from ui.app.child_free_app.components.exercise_card import ExerciseCard
from ui.app.components.cronometer import Cronometer

class ExerciseView(ft.View):
    def __init__(self, appbar: ft.AppBar | None = None) -> None:
        ejercicios = [
            Exercise(id=1, name="Saltos estrella", description="Saltos abriendo brazos y piernas", level=1, category="Resistencia"),
            Exercise(id=2, name="Sentadillas básicas", description="Sentadillas para principiantes", level=1, category="Fuerza"),
            Exercise(id=3, name="Estiramiento de brazos", description="Estirar brazos en diferentes direcciones", level=1, category="Elasticidad"),
            Exercise(id=4, name="Flexiones de brazos", description="Flexiones para fortalecer el tren superior", level=2, category="Fuerza"),
            Exercise(id=5, name="Abdominales", description="Ejercicio para fortalecer el abdomen", level=2, category="Fuerza"),
            Exercise(id=6, name="Caminata rápida", description="Caminata a paso ligero para mejorar resistencia", level=1, category="Cardio"),
        ]
        
        # Categorías para filtrar
        categorias = ["Todos", "Resistencia", "Fuerza", "Elasticidad", "Cardio"]
        
        super().__init__(
            route="/ejercicios",
            appbar=appbar,
            controls=[
                ft.Container(
                    padding=20,
                    expand=True,
                    content=ft.Column([
                        # Barra de progreso semanal
                        ft.Container(
                            padding=10,
                            border_radius=16,
                            bgcolor="green100",
                            content=ft.Column([
                                ft.Row([
                                    ft.Text("Tu progreso semanal", size=16, weight=ft.FontWeight.BOLD, color="green800"),
                                    ft.Text("2/7 días", size=14, color="green700")
                                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                ft.Container(
                                    padding=5,
                                    content=ft.ProgressBar(value=0.28, color="green500", bgcolor="white", height=15, width=float("inf")),
                                )
                            ]),
                            margin=ft.margin.only(bottom=15)
                        ),
                        
                        # Hacemos toda la columna principal scrolleable y expandible
                        ft.Column([
                            ft.Row(
                                spacing=20,
                                vertical_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    # Contenedor para la lista de ejercicios (50% del ancho)
                                    ft.Container(
                                        expand=2,
                                        content=ft.Column([
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
                                                content=ft.Row([
                                                    ft.Container(
                                                        content=ft.Text(cat, size=12, color="green800"),
                                                        bgcolor="green50" if cat == "Todos" else "white",
                                                        border=ft.border.all(1, "green200"),
                                                        border_radius=15,
                                                        padding=ft.padding.symmetric(horizontal=15, vertical=5),
                                                        margin=ft.margin.only(right=5),
                                                    ) for cat in categorias
                                                ], scroll=ft.ScrollMode.AUTO)
                                            ),
                                            
                                            # ListView con altura específica y scroll
                                            ft.Container(
                                                height=400,
                                                content=ft.ListView(
                                                    [
                                                        ExerciseCard(
                                                            exercise=exercise,
                                                            on_click=lambda e, ex=exercise: self._on_exercise_selected(ex)
                                                        ) for exercise in ejercicios
                                                    ],
                                                    spacing=10,
                                                    padding=ft.padding.symmetric(vertical=10),
                                                    auto_scroll=True
                                                ),
                                                border_radius=8,
                                                border=ft.border.all(1, "green100"),
                                            )
                                        ], spacing=10)
                                    ),
                                    
                                    # Contenedor para la visualización y ejecución de ejercicio (50% del ancho)
                                    ft.Container(
                                        expand=2,
                                        border_radius=16,
                                        bgcolor="green50",
                                        padding=16,
                                        content=ft.Column([
                                            ft.Text("¡Ejercítate!", size=18, weight=ft.FontWeight.BOLD, color="green700"),
                                            
                                            # Visualización de ejercicio animada - ahora arriba con altura controlada
                                            ft.Container(
                                                height=200,
                                                content=ft.Lottie(
                                                    "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json",
                                                    width=200,
                                                    height=200,
                                                    repeat=True,
                                                    animate=True
                                                ),
                                                alignment=ft.alignment.center,
                                                margin=ft.margin.only(top=10, bottom=20),
                                            ),
                                            
                                            # Sección de interacción - cronómetro y botón
                                            ft.Container(
                                                content=ft.Column([
                                                    # Cronómetro para el ejercicio
                                                    Cronometer(time=2.0, on_finish=self._on_exercise_finished),
                                                    
                                                    # Botón para marcar como completado
                                                    ft.Container(
                                                        content=ft.ElevatedButton(
                                                            "¡Lo completé!",
                                                            icon=ft.icons.CHECK_CIRCLE,
                                                            style=ft.ButtonStyle(
                                                                color="white",
                                                                bgcolor="green600",
                                                            ),
                                                            width=float("inf"),
                                                            height=45,
                                                            on_click=self._on_exercise_completed
                                                        ),
                                                        margin=ft.margin.only(top=10)
                                                    ),
                                                ]),
                                            ),
                                            
                                            # Banner premium sutilmente promocional
                                            ft.Container(
                                                margin=ft.margin.only(top=15),
                                                border_radius=12,
                                                bgcolor="amber50",
                                                padding=10,
                                                content=ft.Row([
                                                    ft.Icon(ft.icons.STAR, color="amber600", size=20),
                                                    ft.Text("¡Desbloquea más ejercicios con Premium!", size=12, color="amber800"),
                                                ], spacing=5)
                                            )
                                        ], 
                                        spacing=10,
                                        alignment=ft.MainAxisAlignment.START,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                                    )
                                ]
                            )
                        ], scroll=ft.ScrollMode.AUTO, expand=True)
                    ])
                )
            ]
        )
    
    def _on_exercise_selected(self, exercise: Exercise):
        # Método para manejar cuando se selecciona un ejercicio
        print(f"Ejercicio seleccionado: {exercise.name}")
        
    def _on_exercise_finished(self):
        # Método para manejar cuando termina el cronómetro
        print("¡Tiempo finalizado!")
        
    def _on_exercise_completed(self, e):
        # Método para manejar cuando se marca un ejercicio como completado
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
