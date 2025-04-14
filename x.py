from domain.model.model import Tutor, Child, Nutritionist
from navigation_system.manager import ViewManager


class App:
    pass

class FreeChildApp(App):...
class FreeTutorApp(App):...

class PremiumChildApp(App):...
class PremiumTutorApp(App):...

class UserAppMap:
    """
    El mapa de aplicación de usuario devuelve una aplicación en función del tipo de usuario y de la suscripción asociada a este.
    """

    def __init__(self) -> None:
        self._user_app = {
            Child.__name__: FreeChildApp,
            Tutor.__name__: FreeTutorApp,
        }
    
    def __getitem__(self, user: Tutor | Child | Nutritionist | None) -> App | None:
        return self._user_app[user.__class__.__name__] if user else {}
    
    def __iter__(self):
        return iter(self._user_app)
    




class AppManager:
    """
    Recibe una instancia ``User`` o un ``None`` y devuelve un ``ViewManager`` tipado genéricamente, con algún tipo de aplicación si el usuario existe. Si no, devuelve ``None`` para manejar la situación.

    El objetivo de este artefacto es suministrar una aplicación que se arma dinámicamente en función del tipo de usuario y de la suscripción asociada a este. El ``ViewManager`` es el encargado de suministrar eso conforme se navega en la aplicación. 
    """

    def __init__(self, user: Tutor | Child | Nutritionist | None) -> None:
        self._user = user
        self._user_app = UserAppMap()
    
    @property
    def view_manager(self) -> ViewManager[type(App)] | None:
        """
        Devuelve un ``ViewManager`` (tipado genéricamente) de algún tipo de aplicación. Por ejemplo, ``ViewManager[FreeChildApp]``.
        """
        user_data = UserAppMap()[self._user]
        return App() if user_data else None

