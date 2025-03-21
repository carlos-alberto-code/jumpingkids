import flet as ft


class RoutinesView(ft.View):

    def __init__(
            self,
            on_view_exercises_button_click=None,
            on_favorite_button_click=None,
            on_filter_by_favorite_button_click=None,
            on_filter_by_category_button_click=None,
    ) -> None:
        super().__init__()
