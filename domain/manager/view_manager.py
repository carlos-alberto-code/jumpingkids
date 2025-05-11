import flet as ft
from domain.manager.controller import Controller

class ViewManager:
    """
    Gestiona las vistas de la aplicación (Módulos de aplicación).
    
    Esta clase proporciona mecanismos para:
    1. Registrar controladores para diferentes rutas
    2. Obtener vistas reconstruidas bajo demanda
    
    Cada vez que se solicita una vista, se reconstruye completamente,
    lo que garantiza un estado fresco pero puede implicar más tiempo
    de procesamiento en las transiciones.
    
    Ejemplo de uso:
    ```python
    view_manager = ViewManager()
    view_manager["inventory"] = Controller(
        view_class=InventoryView,
        event_class=InventoryEvents,
        service_classes={
            InventoryServiceCore: (InventoryRepositoryAdapter, ProductsRepositoryAdapter),
            StoreServiceCore: (StoreRepositoryAdapter,)
        }
    )
    
    # Obtener la vista instanciada (reconstruida cada vez)
    inventory_view = view_manager["inventory"]  # Retorna un ft.View
    ```
    """

    def __init__(self) -> None:
        self._controllers: dict[str, Controller] = {}

    def __getitem__(self, key: str) -> ft.View:
        if key not in self._controllers:
            raise KeyError(f"Controlador no registrado: {key}")
        controller = self._controllers[key]
        return controller.build()

    def __setitem__(self, key: str, controller: Controller) -> None:
        self._controllers[key] = controller
    
    def keys(self) -> list[str]:
        """Devuelve una lista de las claves de los controladores registrados. Pueden ser usadas como nombres de vistas."""
        return list(self._controllers.keys())
