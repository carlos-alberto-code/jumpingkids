from dataclasses import dataclass
from typing import Literal


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
    suscription: "Subscription | None"


@dataclass
class Nutritionist(User):
    """Representa a un nutricionista de la aplicación. No es necesario que tenga una suscripción."""
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


class Subscription:
    """Representa una suscripción de la aplicación."""
    id: int
    name: str
    description: str
    price: float


class FreeSubscription(Subscription):
    """Representa una suscripción gratuita de la aplicación."""
    def __init__(self):
        self.name = "Free"
        self.description = "Suscripción gratuita"
        self.price = 0.0
    

class PremiumSubscription(Subscription):
    """Representa una suscripción premium de la aplicación."""
    def __init__(self):
        self.name = "Premium"
        self.description = "Suscripción premium"
        self.price = 9.99