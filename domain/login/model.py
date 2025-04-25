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
    subscription_type: SubscriptionType


@dataclass
class Tutor(User):
    children: list['Child']


@dataclass
class Child(User):
    tutor: Tutor
    