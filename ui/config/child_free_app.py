import flet as ft

from interface.event_view import EventView

from domain.routing.controller import Controller
from domain.routing.view_manager import ViewManager


view_manager = ViewManager()

view_manager["home"] = Controller(
    view_class=ft.View,
    event_class=EventView,
    service_classes={

    }
)

view_manager["exercises"] = Controller(
        view_class=ft.View,
        event_class=EventView,
        service_classes={

        }
    )

view_manager["desafios"] = Controller(
        view_class=ft.View,
        event_class=EventView,
        service_classes={

        }
    )

view_manager["personajes"] = Controller(
        view_class=ft.View,
        event_class=EventView,
        service_classes={

        }
    )
