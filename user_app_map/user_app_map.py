from domain.model.model import Tutor, Child
from user_app_map.view_manager import ViewManager


class UserAppMap:
    """
    Mapa de aplicación de usuario que devuelve un ``ViewManager`` en función del tipo de usuario y de la suscripción asociada a este.
    """

    def __init__(self, user) -> None:
        self._user = user
        self._view_manager = ViewManager()
    
    @property
    def view_manager(self) -> ViewManager:
        return self._view_manager