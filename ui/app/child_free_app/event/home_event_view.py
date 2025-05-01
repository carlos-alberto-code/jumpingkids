from interface.service import Service
from interface.view_event import ViewEvent
from ui.app.child_free_app.view.home_view import HomeView


class HomeEventView(ViewEvent):

    def __init__(self, view: HomeView, services: list[Service]) -> None:
        super().__init__(view, services)
