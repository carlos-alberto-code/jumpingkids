from domain.model.model import User
from domain.application.repository.auth import AuthRepositoryPort


class AuthRepositoryAdapter(AuthRepositoryPort):
    
    def __init__(self) -> None:
        super().__init__()
    
    def username_exist(self, value: str) -> bool:
        ...

    def password_exist(self, values: str) -> bool:
        ...
    
    def get_user(self, username: str, password: str) -> User | None:
        
        return User(
            id=1,
            full_name="Romulo Romerito",
            username=username,
            password=password,
        )
