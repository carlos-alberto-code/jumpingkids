from interface.view_event import ViewEvent

from domain.routing.controller import Controller
from domain.routing.view_manager import ViewManager

from ui.app.child_free_app.view.home_view import HomeView
from ui.app.child_free_app.view.personaje import PersonajeView
from ui.app.child_free_app.view.challenges import ChallengesView
from ui.app.child_free_app.view.exercise_view import ExerciseView


view_manager = ViewManager()

view_manager["home"] = Controller(
    view_class=HomeView,
    event_class=ViewEvent,
    service_classes={

    }
)

view_manager["exercises"] = Controller(
        view_class=ExerciseView,
        event_class=ViewEvent,
        service_classes={

        }
    )

view_manager["desafios"] = Controller(
        view_class=ChallengesView,
        event_class=ViewEvent,
        service_classes={

        }
    )

view_manager["personajes"] = Controller(
        view_class=PersonajeView,
        event_class=ViewEvent,
        service_classes={

        }
    )
