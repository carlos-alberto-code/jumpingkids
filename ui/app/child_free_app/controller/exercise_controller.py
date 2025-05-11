from ui.app.child_free_app.event.exercise_view_events import ExerciseViewEvents
from ui.app.child_free_app.view.exercise_view import ExerciseView


class ExerciseController:

    def __init__(self):
        self._exercise_service = ExerciseServiceCore(ExerciseRepositoryAdapter())
        self._exercise_view = ExerciseView()
        self._exercise_view_events = ExerciseViewEvents(
            view=self._exercise_view,
            exercise_service=self._exercise_service
        )
    