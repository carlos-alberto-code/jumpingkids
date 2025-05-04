import flet as ft

class AnimationPanel(ft.Container):
    def __init__(self):
        super().__init__(
            content=ft.Lottie(
                "https://assets2.lottiefiles.com/packages/lf20_9p1qcihj.json",  # Animación infantil
                width=320,
                height=320,
                repeat=True,
                animate=True
            ),
            alignment=ft.alignment.center,
            bgcolor="#F3E5F5",
            border_radius=24,
            padding=30,
            expand=True,
        )
