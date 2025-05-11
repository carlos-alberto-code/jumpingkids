

from domain.manager.repository import Repository
from domain.manager.service import Service
from interface.crud.read import GetAll
from ui.app.child_free_app.dto import ExerciseDTO


class ExerciseServicePort(
    Service,
    GetAll[ExerciseDTO]
):

    def __init__(self, *repositories: Repository) -> None:
        super().__init__(*repositories)