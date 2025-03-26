from hexagon.application.repository import SessionRepositoryPort
from hexagon.domain.model import Child, Tutor


class SessionRepositoryAdapter(SessionRepositoryPort):
    def __init__(self) -> None:
        super().__init__()
    
    def get_user(self, username: str, password: str) -> Tutor | Child:
        ...