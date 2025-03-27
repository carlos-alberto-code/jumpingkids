from dataclasses import dataclass
from typing import Optional


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
    created_by: "Nutritionist"
    verified_by: list["Nutritionist"] | None = None


@dataclass
class User:
    id: int
    full_name: str
    username: str
    password: str


@dataclass
class Nutritionist(User):
    """
    Represents a nutritionist who can create and verify routines.
    """
    routines_created: list[Routine] | None = None
    routines_verified: list[Routine] | None = None


@dataclass
class Tutor(User):
    id: int
    children: list["Child"]


@dataclass
class Child(User):
    id: int
    tutor: Tutor | None = None
    favorite_routines: list[Routine] | None = None
