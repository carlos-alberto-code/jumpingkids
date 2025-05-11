
from dataclasses import dataclass


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