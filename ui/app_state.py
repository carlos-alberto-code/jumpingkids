import flet as ft

# from domain.app import App
from domain.model.model import User


class AppState:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._user: User
        # self._app: JApp
        
    @property
    def user(self) -> User:
        return self._user
    
    @user.setter
    def user(self, value: User) -> None:
        self._user = value

    # @property
    # def app(self) -> App:
    #     return self._app

    # @app.setter
    # def app(self, value: App) -> None:
    #     self._app = value
