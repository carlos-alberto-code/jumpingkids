from dataclasses import dataclass
from typing import List

@dataclass
class SubscriptionType:
    id: int
    name: str


@dataclass
class User:
    id: int
    username: str
    password: str
    full_name: str


@dataclass
class Tutor(User):
    children: list['Child']
    subscription_type: SubscriptionType


@dataclass
class Child(User):
    tutor: Tutor
    favorite_routines: List['Routine']


@dataclass
class Category:
    id: int
    name: str
    routines: List['Routine']

@dataclass
class Routine:
    id: int
    name: str
    description: str
    categories: List[Category]
    exercises: List['Exercise']
    subscription_types: List[SubscriptionType]

@dataclass
class Exercise:
    id: int
    name: str
    description: str
    subscription_types: List[SubscriptionType]
