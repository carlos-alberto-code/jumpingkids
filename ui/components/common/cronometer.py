import flet as ft
import time
from enum import Enum
from threading import Thread


class CronometerState(Enum):
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    FINISHED = "finished"


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
    
    def update_time(self, seconds: float) -> None:
        """Actualiza la visualización del tiempo en formato MM:SS"""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        self.value = f"{minutes:02d}:{seconds:02d}"


class CronometerControls(ft.Row):
    """
    Componente que contiene los botones de control del cronómetro
    """
    def __init__(self, on_play_click=None, on_pause_click=None, on_reset_click=None, accent_color=None, button_size=None) -> None:
        self._on_play = on_play_click
        self._on_pause = on_pause_click
        self._on_reset = on_reset_click
                
        self._play_button = ft.IconButton(
            icon=ft.Icons.PLAY_ARROW,
            on_click=on_play_click if on_play_click else None,
            icon_color=accent_color,
            icon_size=button_size,
        )

        self._pause_button = ft.IconButton(
            icon=ft.Icons.PAUSE,
            on_click=on_pause_click if on_pause_click else None,
            icon_color=accent_color,
            icon_size=button_size,
        )
        
        self._reset_button = ft.IconButton(
            icon=ft.Icons.RESTART_ALT,
            on_click=on_reset_click if on_reset_click else None,
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
        self._on_finish = on_finish
        self._initial_time = time
        self._current_time = time
        self._state = CronometerState.READY
        self._timer_thread = None
        
        # Componentes de UI
        self._display = TimeDisplay()
        
        self._cronometer_controls = CronometerControls(
            on_play_click=self._on_play_click,
            on_pause_click=self._on_pause_click,
            on_reset_click=self._on_reset_click,
        )
        
        # Inicializar la visualización del tiempo
        self._update_time_display(time * 60)
        
        super().__init__(
            content=ft.Container(
                padding=20,
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=self._display,
                            margin=ft.margin.symmetric(vertical=20),
                        ),
                        self._cronometer_controls,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                border_radius=10,
            ),
            elevation=4,
        )
    
    def _update_time_display(self, seconds: float) -> None:
        """Actualiza el display de tiempo"""
        self._display.update_time(seconds)
    
    def _on_play_click(self, e) -> None:
        """Maneja el clic en el botón de play"""
        if self._state == CronometerState.READY or self._state == CronometerState.PAUSED:
            self._start_timer()
    
    def _on_pause_click(self, e) -> None:
        """Maneja el clic en el botón de pausa"""
        if self._state == CronometerState.RUNNING:
            self._pause_timer()
    
    def _on_reset_click(self, e) -> None:
        """Reinicia el cronómetro a su estado inicial"""
        self._stop_timer()
        self._current_time = self._initial_time
        self._update_time_display(self._current_time * 60)
        self._state = CronometerState.READY
        self.update()
    
    def _start_timer(self) -> None:
        """Inicia el cronómetro"""
        if self._current_time <= 0:
            return
        
        self._state = CronometerState.RUNNING
        
        if not self._timer_thread or not self._timer_thread.is_alive():
            self._timer_thread = Thread(target=self._run_timer)
            self._timer_thread.daemon = True
            self._timer_thread.start()
    
    def _pause_timer(self) -> None:
        """Pausa el cronómetro"""
        self._state = CronometerState.PAUSED
    
    def _stop_timer(self) -> None:
        """Detiene el cronómetro completamente"""
        self._state = CronometerState.FINISHED
    
    def _run_timer(self) -> None:
        """Función que ejecuta la cuenta regresiva en un hilo separado"""
        start_time = time.time()
        elapsed_time = 0
        
        while self._state == CronometerState.RUNNING and self._current_time > 0:
            # Si está en pausa, actualizar el tiempo de inicio para mantener la coherencia
            if self._state == CronometerState.PAUSED:
                start_time = time.time() - elapsed_time
                while self._state == CronometerState.PAUSED:
                    if self._state == CronometerState.FINISHED:
                        return
                    time.sleep(0.1)
                # Reiniciar si se reanudó desde pausa
                start_time = time.time() - elapsed_time
            
            # Calcular tiempo transcurrido y restante
            elapsed_time = time.time() - start_time
            self._current_time = max(0, self._initial_time - elapsed_time / 60)
            
            # Actualizar UI de forma segura
            self._update_time_display(self._current_time * 60)
            
            # Usar el método page.update desde el contexto correcto
            if self.page:
                self.page.update()
            
            # Verificar si terminó
            if self._current_time <= 0:
                self._timer_finished()
                break
            
            # Pequeña pausa para no sobrecargar la CPU
            time.sleep(0.1)
    
    def _timer_finished(self) -> None:
        """Maneja la finalización del cronómetro"""
        self._state = CronometerState.FINISHED
        self._update_time_display(0)
        
        if self.page:
            self.page.update()
        
        if self._on_finish:
            self._on_finish()


def main(page: ft.Page) -> None:
    """Función de ejemplo para probar el componente"""
    page.theme_mode = ft.ThemeMode.LIGHT
    
    cronometer = Cronometer(time=0.10)
    
    page.add(cronometer)

if __name__ == "__main__":
    ft.app(main)