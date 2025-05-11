import flet as ft

from domain.manager.event import ViewEvent
from domain.manager.service import Service

from domain.app.child_free_app.exercise.exercise_service_core import ExerciseServiceCore

from ui.app.child_free_app.view.exercise_view import ExerciseView
from ui.app.child_free_app.model import CategoryDTO, ExerciseDTO, LevelDTO
from ui.app_state import AppState


class ExerciseViewEvent(ViewEvent[ExerciseView]):

    def __init__(self, view: ExerciseView, services: dict[type[Service], Service]) -> None:
        super().__init__(view, services)
        self._exercise_service = self.get_service(ExerciseServiceCore)
        
        self._view.exercises = self._exercise_service.get_all()
        self._view.categories = self._exercise_service.get_categories()
        self._view.levels = self._exercise_service.get_levels()
        self._view.update()
    
    def _connect_events(self) -> None:
        self._view.on_submit = self._on_submit
        self._view.on_filter_by_level = self._on_filter_by_level
        self._view.on_filter_by_category = self._on_filter_by_category
        self._view.on_view_exercise_details = self._on_view_exercise_details
        self._view.on_favorite_exercise_click = self._on_favorite_exercise_click
        
    def _on_submit(self, event: ft.ControlEvent):
        control: ft.TextField = event.control
        text = control.value
        if text:
            exercises: list[ExerciseDTO] | None = self._exercise_service.search(text)
            if exercises:
                self._view.exercises = exercises
                self._view.update()
    
    def _on_filter_by_level(self, event: ft.ControlEvent):
        level: LevelDTO = event.control.data
        if level:
            exercises: list[ExerciseDTO] | None = self._exercise_service.filter_by_level_id(level.id)
            if exercises:
                self._view.exercises = exercises
                self._view.update()

    def _on_filter_by_category(self, event: ft.ControlEvent):
        category: CategoryDTO = event.control.data
        if category:
            exercises: list[ExerciseDTO] | None = self._exercise_service.filter_by_category_id(category.id)
            if exercises:
                self._view.exercises = exercises
                self._view.update()
    
    def _on_view_exercise_details(self, event: ft.ControlEvent):
        exercise: ExerciseDTO = event.control.data
        if exercise:
            self._view.update_panel(exercise)
            self._view.update()
    
    def _on_favorite_exercise_click(self, event: ft.ControlEvent):
        exercise: ExerciseDTO = event.control.data
        if exercise:
            user = AppState().user
            self._exercise_service.add_favorite_exercise(user.id, exercise.id)
    