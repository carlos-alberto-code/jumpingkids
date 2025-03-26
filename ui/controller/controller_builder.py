from flet import AppBar

from ui.view import RoutinesView
from ui.controller import Controller
from ui.controller import RoutinesViewController

from hexagon.application.core import UserServiceCore
from hexagon.application.core import RoutinesServiceCore

from infrastructure.adapter.user_repository_adapter import UserRepositoryAdapter
from infrastructure.adapter.routines_repository_adapter import RoutinesRepositoryAdapter


class ControllersBuilder:

    def __init__(self, appbar: AppBar) -> None:
        self._appbar = appbar
        self._controllers: dict[str, Controller] = {}
    
    @property
    def controllers(self) -> dict[str, Controller]:
        return self._controllers
        
    def build_routines_controller(self) -> None:
        self._controllers["routines"] = RoutinesViewController(
            routines_view=RoutinesView(
                appbar=self._appbar
            ),
            user_service=UserServiceCore(
                user_repository=UserRepositoryAdapter(),
                routines_repository=RoutinesRepositoryAdapter()
            ),
            routines_service=RoutinesServiceCore(
                routines_repository=RoutinesRepositoryAdapter()
            )
        )