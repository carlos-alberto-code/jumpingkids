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
    # created_by: "Nutritionist"


@dataclass
class User:
    """Representa a un usuario de la aplicación."""
    id: int
    full_name: str
    username: str
    password: str


@dataclass
class Nutritionist(User):
    """Representa a un nutricionista de la aplicación."""
    routines_created: list[Routine] | None = None


@dataclass
class Tutor(User):
    """Representa a un tutor de la aplicación."""
    id: int
    children: list["Child"]


@dataclass
class Child(User):
    """Representa a un niño de la aplicación."""
    id: int
    tutor: Tutor
    favorite_routines: list[Routine] | None = None
