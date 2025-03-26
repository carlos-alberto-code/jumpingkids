from dataclasses import dataclass
from datetime import date


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
    birth_date: date
    username: str
    password: str


@dataclass
class Tutor(User):
    id: int
    children: list["Child"]


@dataclass
class Child(User):
    id: int
    tutor: Tutor
    favorite_routines: list[Routine]
