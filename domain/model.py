from dataclasses import dataclass


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
    favorite_routines: list['Routine']


@dataclass
class Category:
    id: int
    name: str
    routines: list['Routine']


@dataclass
class Routine:
    id: int
    name: str
    description: str
    categories: list[Category]
    exercises: list['Exercise']
    subscription_types: list[SubscriptionType]


@dataclass
class Exercise:
    id: int
    name: str
    description: str
    subscription_types: list[SubscriptionType]
