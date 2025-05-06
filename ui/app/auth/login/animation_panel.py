import flet as ft


class AnimationPanel(ft.Container):
    def __init__(self):
        super().__init__(
            width=500,
            bgcolor="#2D2242",
            padding=0,  # Eliminado el padding para que quede pegado a la izquierda
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=350,
                        height=350,
                        content=ft.Lottie(
                            "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json",
                            repeat=True,
                            animate=True,
                        )
                    ),
                    # Línea decorativa en la parte inferior
                    ft.Container(
                        width=150,
                        height=4,
                        border_radius=ft.border_radius.all(10),
                        bgcolor="#444444",
                        margin=ft.margin.only(top=50)
                    )
                ]
            )
        )
