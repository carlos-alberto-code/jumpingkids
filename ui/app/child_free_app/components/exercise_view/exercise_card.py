import flet as ft

from ui.app.child_free_app.dto import ExerciseDTO


class Tag(ft.Container):

    def __init__(self, text: str):
        super().__init__(
            content=ft.Text(text),
            padding=ft.padding.only(left=4, right=4, top=2, bottom=2),
            bgcolor=ft.Colors.BLUE_50,
            border_radius=ft.border_radius.all(4),
            margin=ft.margin.only(right=4),
            alignment=ft.alignment.center,
        )
        

class ExerciseCard(ft.Card):

    def __init__(
        self,
        exercise: ExerciseDTO,
        on_click=None,
    ) -> None:
        super().__init__()
        self._exercise = exercise
        self._on_click = on_click

        self.content = ft.ListTile(
            leading=ft.Icon(ft.Icons.FITNESS_CENTER),
            title=ft.Text(exercise.name),
            subtitle=ft.Column(
                [
                    ft.Text(exercise.description),
                    ft.Row(
                        [
                            Tag(exercise.category),
                            Tag(exercise.level),
                            Tag(f"{exercise.duration} mins"),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ]
            ),
            trailing=ft.IconButton(
                icon=ft.Icons.PLAY_ARROW,
                on_click=self._on_click,
                data=exercise,
            ),
        )
            
        