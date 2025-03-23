from dataclasses import dataclass


@dataclass
class Category:
    id: int
    name: str
    routines: list["Routine"]


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
    categories: list[Category]
    exercises: list[Exercise]


@dataclass
class RoutineExercise:
    routine: Routine
    exercise: Exercise


@dataclass
class Tutor:
    id: int
    full_name: str
    children: list["Child"]


@dataclass
class Child:
    id: int
    full_name: str
    age: int
    tutor: Tutor
