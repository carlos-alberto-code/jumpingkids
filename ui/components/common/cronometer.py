import flet as ft
import time
from enum import Enum
from threading import Thread, Event


class CronometerState(Enum):
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    FINISHED = "finished"


class TimerLogic:
    """
    Lógica del cronómetro: maneja el tiempo, estado y callbacks.
    """
    def __init__(self, minutes: float, on_tick=None, on_finish=None):
        self._initial_minutes = minutes
        self._current_seconds = int(minutes * 60)
        self._state = CronometerState.READY
        self._on_tick = on_tick
        self._on_finish = on_finish
        self._thread = None
        self._stop_event = Event()

    @property
    def state(self):
        return self._state

    @property
    def current_seconds(self):
        return self._current_seconds

    def start(self):
        if self._state in [CronometerState.READY, CronometerState.PAUSED]:
            self._state = CronometerState.RUNNING
            self._stop_event.clear()
            if not self._thread or not self._thread.is_alive():
                self._thread = Thread(target=self._run, daemon=True)
                self._thread.start()

    def pause(self):
        if self._state == CronometerState.RUNNING:
            self._state = CronometerState.PAUSED

    def reset(self):
        self._stop_event.set()
        self._state = CronometerState.READY
        self._current_seconds = int(self._initial_minutes * 60)
        if self._on_tick:
            self._on_tick(self._current_seconds)

    def stop(self):
        self._stop_event.set()
        self._state = CronometerState.FINISHED

    def _run(self):
        last_tick = time.time()
        while self._state == CronometerState.RUNNING and self._current_seconds > 0:
            if self._stop_event.is_set():
                return
            if self._state == CronometerState.PAUSED:
                last_tick = time.time()
                while self._state == CronometerState.PAUSED:
                    if self._stop_event.is_set():
                        return
                    time.sleep(0.1)
                last_tick = time.time()
            now = time.time()
            elapsed = now - last_tick
            if elapsed >= 1:
                self._current_seconds = max(0, self._current_seconds - int(elapsed))
                last_tick = now
                if self._on_tick:
                    self._on_tick(self._current_seconds)
            if self._current_seconds <= 0:
                self._state = CronometerState.FINISHED
                if self._on_tick:
                    self._on_tick(0)
                if self._on_finish:
                    self._on_finish()
                return
            time.sleep(0.1)


class TimeDisplay(ft.Text):
    """
    Componente para mostrar el tiempo en formato MM:SS durante la cuenta regresiva
    """
    def __init__(self, text_color=None, size=None) -> None:
        super().__init__(
            value="00:00",
            text_align=ft.TextAlign.CENTER,
            color=text_color,
            size=size,
        )

    def update_time(self, seconds: int) -> None:
        """Actualiza la visualización del tiempo en formato MM:SS"""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        self.value = f"{minutes:02d}:{seconds:02d}"


class CronometerControls(ft.Row):
    """
    Componente que contiene los botones de control del cronómetro
    """
    def __init__(self, on_play_click=None, on_pause_click=None, on_reset_click=None, accent_color=None, button_size=None) -> None:
        self._play_button = ft.IconButton(
            icon=ft.Icons.PLAY_ARROW,
            on_click=on_play_click,
            icon_color=accent_color,
            icon_size=button_size,
        )
        self._pause_button = ft.IconButton(
            icon=ft.Icons.PAUSE,
            on_click=on_pause_click,
            icon_color=accent_color,
            icon_size=button_size,
        )
        self._reset_button = ft.IconButton(
            icon=ft.Icons.RESTART_ALT,
            on_click=on_reset_click,
            icon_color=accent_color,
            icon_size=button_size,
        )
        super().__init__(
            controls=[
                self._play_button,
                self._pause_button,
                self._reset_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )


class Cronometer(ft.Card):
    """
    Componente principal de cronómetro para cuenta regresiva.
    """
    def __init__(
        self,
        time: float = 15.0,
        on_finish=None,
    ) -> None:
        super().__init__()
        self._display = TimeDisplay()
        self._logic = TimerLogic(
            minutes=time,
            on_tick=self._on_tick,
            on_finish=self._on_finish_wrapper(on_finish),
        )
        self._controls = CronometerControls(
            on_play_click=self._on_play_click,
            on_pause_click=self._on_pause_click,
            on_reset_click=self._on_reset_click,
        )
        self.content = ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=self._display,
                        margin=ft.margin.symmetric(vertical=20),
                    ),
                    self._controls,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            border_radius=10,
        )
        self.elevation = 4
        self._on_tick(self._logic.current_seconds)

    def _on_tick(self, seconds: int):
        self._display.update_time(seconds)
        if self.page:
            self.page.update()

    def _on_finish_wrapper(self, user_on_finish):
        def wrapper():
            if self.page:
                self.page.update()
            if user_on_finish:
                user_on_finish()
        return wrapper

    def _on_play_click(self, event: ft.ControlEvent):
        self._logic.start()

    def _on_pause_click(self, event: ft.ControlEvent):
        self._logic.pause()

    def _on_reset_click(self, event: ft.ControlEvent):
        self._logic.reset()
        if self.page:
            self.page.update()


def main(page: ft.Page) -> None:
    """Función de ejemplo para probar el componente"""
    page.theme_mode = ft.ThemeMode.LIGHT
    cronometer = Cronometer(time=0.10)
    page.add(cronometer)

if __name__ == "__main__":
    ft.app(main)