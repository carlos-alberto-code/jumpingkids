import flet as ft

from ui.controller import ControllersBuilder
from ui.view.appbar import JumpingKidsAppbar

from hexagon.domain.model import Child, Tutor
from hexagon.application.core import ChildSessionServiceCore

from infrastructure.adapter import ChildSessionRepositoryAdapter


class AppViewBuilder:

    def __init__(
            self,
    ) -> None:
        session_service = ChildSessionServiceCore(child_session_repository=ChildSessionRepositoryAdapter())
        self._user: Child | None = session_service.login("cabh")
        if self._user:
            self._appbar = JumpingKidsAppbar("Rutinas", self._user.username)
            self._controllers = ControllersBuilder(appbar=self._appbar)
            self._views: dict[str, ft.View] = {
                route: controller.view
                for route, controller in self._controllers
            }
        else:
            raise Exception("El usuario no existe!")
    
    def __iter__(self):
        return iter(self._views.items())

    @property
    def views(self) -> dict[str, ft.View]:
        return self._views
    # Definir aquí los eventos para los actions del appbar
    