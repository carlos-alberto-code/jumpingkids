
from dataclasses import dataclass


@dataclass
class ExerciseDTO:
    id: int
    name: str
    description: str
    category: str
    level: str
    duration: int
