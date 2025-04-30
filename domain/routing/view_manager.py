from domain.routing.module import Module
from interface.module_view import ModuleView


class ViewManager:
    """
    Gestiona las vistas de la aplicación utilizando Módulos.
    
    Esta clase proporciona mecanismos para:
    1. Registrar Módulos para diferentes rutas
    2. Obtener vistas reconstruidas bajo demanda
    
    Cada vez que se solicita una vista, se reconstruye completamente,
    lo que garantiza un estado fresco pero puede implicar más tiempo
    de procesamiento en las transiciones.
    
    Ejemplo de uso:
    ```python
    view_manager = ViewManager[type(App)]()
    view_manager["inventory"] = Module(
        name="Inventario",
        icon=...,  # icono correspondiente
        route="/inventory",
        controller=Controller(
            view_class=InventoryView,
            event_class=InventoryEvents,
            service_classes={
                InventoryServiceCore: (InventoryRepositoryAdapter, ProductsRepositoryAdapter),
                StoreServiceCore: (StoreRepositoryAdapter,)
            }
        )
    )
    
    # Obtener la vista instanciada (reconstruida cada vez)
    inventory_view = view_manager["inventory"]  # Retorna un ft.Control
    ```
    """

    def __init__(self) -> None:
        self._modules: dict[str, Module] = {}

    def __getitem__(self, key: str) -> ModuleView:
        if key not in self._modules:
            raise KeyError(f"Módulo no registrado: {key}")
        module = self._modules[key]
        return module.controller.build()

    def __setitem__(self, key: str, module: Module) -> None:
        self._modules[key] = module
    
    def keys(self) -> list[str]:
        """Devuelve una lista de las claves de los módulos registrados. Pueden ser usadas como nombres de vistas."""
        return list(self._modules.keys())
