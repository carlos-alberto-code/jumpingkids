from dataclasses import dataclass


@dataclass
class TutorCreate:
    full_name: str
    username: str
    password: str
    subscription_type_id: int
    