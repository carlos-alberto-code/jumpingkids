from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Exercise:
    id: int
    name: str
    description: str


@dataclass
class Routine:
    id: int
    name: str
    description: str
    category: Category


@dataclass
class RoutineExercise:
    routine: Routine
    exercise: Exercise
