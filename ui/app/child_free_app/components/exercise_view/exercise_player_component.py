import flet as ft
from domain.model.model import Exercise
from ui.app.components.cronometer import Cronometer

class ExercisePlayerComponent(ft.Container):
    """Componente que muestra la visualización y ejecución de un ejercicio."""
    
    def __init__(self, on_exercise_finished=None, on_exercise_completed=None):
        """
        Inicializa el componente de visualización y ejecución de ejercicio.
        
        Args:
            on_exercise_finished (callable): Función a ejecutar cuando finaliza el cronómetro
            on_exercise_completed (callable): Función a ejecutar cuando se completa el ejercicio
        """
        self.on_exercise_finished = on_exercise_finished or (lambda: None)
        self.on_exercise_completed = on_exercise_completed or (lambda e: None)
        self.current_exercise = None
        self.animation_url = "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json"
        
        # Crear cronómetro
        self.cronometer = Cronometer(time=2.0, on_finish=self._handle_exercise_finished)
        
        # Crear botón de completar ejercicio
        self.complete_button = ft.ElevatedButton(
            "¡Lo completé!",
            icon=ft.icons.CHECK_CIRCLE,
            style=ft.ButtonStyle(
                color="white",
                bgcolor="green600",
            ),
            width=float("inf"),
            height=45,
            on_click=self._handle_exercise_completed
        )
        
        # Crear animación de ejercicio
        self.exercise_animation = ft.Lottie(
            self.animation_url,
            width=200,
            height=200,
            repeat=True,
            animate=True
        )
        
        # Crear contenido del componente
        content = ft.Column([
            ft.Text("¡Ejercítate!", size=18, weight=ft.FontWeight.BOLD, color="green700"),
            
            # Visualización de ejercicio animada
            ft.Container(
                height=200,
                content=self.exercise_animation,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=10, bottom=20),
            ),
            
            # Sección de interacción - cronómetro y botón
            ft.Container(
                content=ft.Column([
                    # Cronómetro para el ejercicio
                    self.cronometer,
                    
                    # Botón para marcar como completado
                    ft.Container(
                        content=self.complete_button,
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
        
        # Inicializar el contenedor con los estilos adecuados
        super().__init__(
            content=content,
            expand=2,
            border_radius=16,
            bgcolor="green50",
            padding=16,
        )
    
    def set_exercise(self, exercise):
        """
        Establece el ejercicio actual a visualizar.
        
        Args:
            exercise (Exercise): Ejercicio a mostrar
        """
        self.current_exercise = exercise
        
        # Aquí se podría actualizar la animación según el tipo de ejercicio
        # Por ahora, actualizamos el título del componente
        if exercise:
            self.content.controls[0].value = f"¡Ejercítate! - {exercise.name}" # type: ignore
            self.update()
    
    def set_animation(self, animation_url):
        """
        Cambia la animación mostrada.
        
        Args:
            animation_url (str): URL de la animación Lottie
        """
        self.animation_url = animation_url
        self.exercise_animation.src = animation_url
        self.update()
    
    def start_timer(self, minutes=2.0):
        """
        Inicia el cronómetro con la cantidad de minutos especificada.
        
        Args:
            minutes (float): Minutos que durará el ejercicio
        """
        self.cronometer.set_time(minutes) # type: ignore
        self.cronometer.start() # type: ignore
    
    def _handle_exercise_finished(self):
        """Maneja el evento cuando termina el cronómetro."""
        if self.on_exercise_finished:
            self.on_exercise_finished()
    
    def _handle_exercise_completed(self, e):
        """
        Maneja el evento cuando se marca un ejercicio como completado.
        
        Args:
            e: Evento del botón
        """
        if self.on_exercise_completed:
            self.on_exercise_completed(e)
    
    def set_on_exercise_finished(self, callback):
        """
        Establece el callback para el evento de finalización de ejercicio.
        
        Args:
            callback (callable): Función a ejecutar
        """
        self.on_exercise_finished = callback
        self.cronometer.set_on_finish(callback) # type: ignore
    
    def set_on_exercise_completed(self, callback):
        """
        Establece el callback para el evento de ejercicio completado.
        
        Args:
            callback (callable): Función a ejecutar
        """
        self.on_exercise_completed = callback
        self.complete_button.on_click = callback