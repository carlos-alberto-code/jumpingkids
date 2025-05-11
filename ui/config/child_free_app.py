from interface.view_event import ViewEvent

from domain.routing.controller import Controller
from domain.routing.view_manager import ViewManager

from ui.app.child_free_app.view.exercise_view import ExerciseView


view_manager = ViewManager()

view_manager["exercises"] = Controller(
        view_class=ExerciseView,
        event_class=ViewEvent,
        service_classes={
            ExerciseServicePort: [ExerciseRepositoryPort]
        }
    )
