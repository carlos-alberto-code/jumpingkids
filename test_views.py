import flet as ft
from ui.app.child_free_app.view.home_view import HomeView
from ui.app.child_free_app.view.challenges import ChallengesView
from ui.app.child_free_app.view.exercise_view import ExerciseView
from ui.app.child_free_app.view.personaje import PersonajeView


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.views.append(HomeView())

    page.go("/home")
    page.update()

ft.app(main)