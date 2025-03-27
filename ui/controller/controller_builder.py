from flet import AppBar, NavigationBar

from ui.view import RoutinesView
from ui.controller import Controller

from hexagon.application.core import UserServiceCore
from hexagon.application.core import RoutinesServiceCore

from infrastructure.adapter.user_repository_adapter import UserRepositoryAdapter
from infrastructure.adapter.routines_repository_adapter import RoutinesRepositoryAdapter


class ControllersBuilder:
    """
    Esta clase tiene la responsabilidade de construir los controladores de la aplicación. Para armar un controlador, es necesario crear un nuevo método privado en donde se importará el controlador a construir y se inicializará con los parámetros necesarios. La clase es un iterable, por lo que se puede iterar sobre los controladores construidos.
    """

    def __init__(self, appbar: AppBar, navigation: NavigationBar) -> None:
        self._appbar = appbar
        self._navigation = navigation
        self._controllers: dict[str, Controller] = {}
        self._build()
    
    def __iter__(self):
        return iter(self._controllers.items())

    def _build(self) -> None:
        """
        Este método es el punto de entrada para construir los controladores. Se encarga de llamar a los métodos privados que construyen cada controlador.
        """
        self._build_routines_controller()
        
    def _build_routines_controller(self) -> None:
        from ui.controller import RoutinesViewController
        self._controllers["routines"] = RoutinesViewController(
            routines_view=RoutinesView(
                appbar=self._appbar,
                navigation=self._navigation
            ),
            user_service=UserServiceCore(
                user_repository=UserRepositoryAdapter(),
                routines_repository=RoutinesRepositoryAdapter()
            ),
            routines_service=RoutinesServiceCore(
                routines_repository=RoutinesRepositoryAdapter()
            )
        )
