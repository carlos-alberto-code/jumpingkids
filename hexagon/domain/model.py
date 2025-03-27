from dataclasses import dataclass
from datetime import date
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


@dataclass
class User:
    id: int
    full_name: str
    username: str
    password: str


@dataclass
class Tutor(User):
    id: int
    children: list["Child"]


@dataclass
class Child(User):
    id: int
    tutor: Tutor | None = None
    favorite_routines: list[Routine] | None = None
