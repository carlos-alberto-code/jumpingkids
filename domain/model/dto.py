import flet as ft
from dataclasses import dataclass

from domain.manager.view_manager import ViewManager


@dataclass
class App:
    theme: ft.Theme
    view_manager: ViewManager

    @property
    def default_view(self) -> ft.View:
        try:
            return self.view_manager["/"]
        except KeyError:
            raise KeyError("Default view not found in view manager.")


@dataclass
class ExerciseDTO:
    id: int
    name: str
    description: str
    category: str
    level: str
    duration: int


@dataclass
class CategoryDTO:
    id: int
    name: str


@dataclass
class LevelDTO:
    id: int
    name: str