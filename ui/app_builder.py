import flet as ft

from ui.controller import ControllersBuilder
from ui.view.appbar import JumpingKidsAppbar

from hexagon.domain.model import Child, Tutor
from hexagon.application.core import SessionServiceCore

from infrastructure.adapter import SessionRepositoryAdapter





class AppViewBuilder:

    def __init__(
            self,
    ) -> None:
        session_service = SessionServiceCore(session_repository=SessionRepositoryAdapter())
        self._user: Tutor | Child | None = session_service.login("CABH_000", "cabh_000")
        if self._user:
            self._appbar = JumpingKidsAppbar("Rutinas", self._user.username)
            self._controllers = ControllersBuilder(appbar=self._appbar).controllers
        else:
            raise Exception("El usuario no existe!")
    
    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id: int) -> None:
        self._user_id = user_id

    @property
    def views(self) -> dict[str, dict[str, ft.View]]:
        return {
            route: controller.view
            for route, controller in self._controllers.items()
        }

    # Definir aquí los eventos para los actions del appbar
    