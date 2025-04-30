"""
En este archivo voy a diseñar clases que permitan que la app pueda devolver los recursos necesarios a un usuario en función del tipo de usuario y el tipo de suscripción.

La variabilidad es la siguiente:
- Un ``Child`` con suscripción ``Free`` tendrá acceso a cierto módulos, ciertas características de estos y a una apariencia de la aplicación que refleje su suscripción y que es un niño.
- Un ``Child`` con suscripción ``Premium`` tendrá acceso a más módulos, más características de estos y a una apariencia de la aplicación que refleje su suscripción y que es un niño.
- Un ``Tutor`` con suscripción ``Free`` tendrá acceso a cierto módulos, ciertas características de estos y a una apariencia de la aplicación que refleje su suscripción y que es un tutor.
- Un ``Tutor`` con suscripción ``Premium`` tendrá acceso a más módulos, más características de estos y a una apariencia de la aplicación que refleje su suscripción y que es un tutor.

Se está diseñando el sistema de esta forma para que permita añadir más tipos de usuario y más tipos de suscripción en el futuro. sin que haya que modificar el código existente, sino simplemente añadir nuevas características o mejorar las existentes de una forma más sencilla y rápida.
"""

from user_app_map.user_app_map import UserAppMap
from ui.routes.manager.view_manager import ViewManager
from domain.application.core import LoginServiceCore
from infrastructure.adapter import LoginRepositoryAdapter

# Podría tener una especie de mapeador que arme varios ``ViewManager`` en función de los tipos de usuario y suscripción. Una vez que se identifique al usuario, devuelve el ``ViewManager`` correspondiente.

login_service = LoginServiceCore(LoginRepositoryAdapter())
user = login_service.login(username="username", password="password")

view_manager: ViewManager = UserAppMap(user).view_manager # Devuelve el ``ViewManager`` correspondiente al usuario autenticado.
view_manager["Inicio"] # Devuelve el módulo de aplicación "Inicio" instanciado sólo cuando se necesita.

