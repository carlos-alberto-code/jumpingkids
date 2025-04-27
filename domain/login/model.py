from enum import Enum, auto
from dataclasses import dataclass


class SubscriptionType(Enum):
    FREE = auto()
    PREMIUM = auto()


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
    