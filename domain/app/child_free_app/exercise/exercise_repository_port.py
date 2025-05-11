from domain.manager.repository import Repository


class ExerciseRepositoryPort(
    Repository
):
    def __init__(self) -> None:
        super().__init__()