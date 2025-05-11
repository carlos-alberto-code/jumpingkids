from domain.manager.controller import Controller
from domain.manager.view_manager import ViewManager

from ui.app.child_free_app.view.exercise_view import ExerciseView
from ui.app.child_free_app.event.exercise_view_event import ExerciseViewEvent


view_manager = ViewManager()

view_manager["exercises"] = Controller(
        view_class=ExerciseView,
        event_class=ExerciseViewEvent,
        service_classes={
            ExerciseServicePort: [ExerciseRepositoryPort]
        }
    )
