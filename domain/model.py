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
