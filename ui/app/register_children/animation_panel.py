import flet as ft

class AnimationPanel(ft.Container):
    """
    Panel de animación mejorado para la vista de registro de niños.
    Muestra una animación atractiva junto con texto motivacional.
    """
    def __init__(self):
        # URL de animación Lottie adecuada para niños
        animation_url = "https://assets9.lottiefiles.com/packages/lf20_tiviyc6j.json"  # Niños jugando
        
        # Texto motivacional
        motivational_text = [
            "¡Haz que tus hijos se ejerciten divirtiéndose!",
            "Actividad física + diversión = niños saludables",
            "Acompaña a tus hijos en su desarrollo físico"
        ]
        
        super().__init__(
            content=ft.Column(
                [
                    # Título
                    ft.Text(
                        "¡Bienvenido a JumpingKids!",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="white",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    # Subtítulo
                    ft.Text(
                        "Un lugar divertido para ejercitarse",
                        size=16,
                        italic=True,
                        color="white",
                        opacity=0.8,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    # Animación
                    ft.Container(
                        content=ft.Lottie(
                            animation_url,
                            width=300,
                            height=300,
                            repeat=True,
                            animate=True,
                        ),
                        alignment=ft.alignment.center,
                        margin=ft.margin.symmetric(vertical=20),
                    ),
                    
                    # Tarjetas con texto motivacional
                    *[self._create_motivational_card(text) for text in motivational_text],
                    
                    # Logo o marca de agua
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "JumpingKids",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color="white",
                                ),
                                ft.Text(
                                    "Estimulando a niños entre 10 y 15 años",
                                    size=12,
                                    color="white",
                                    opacity=0.7,
                                ),
                            ],
                            spacing=0,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        margin=ft.margin.only(top=40),
                        alignment=ft.alignment.center,
                    ),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.only(
                top_right=24,
                bottom_right=24
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#673AB7", "#4527A0"],
            ),
            padding=30,
            expand=True,
        )
    
    def _create_motivational_card(self, text):
        """Crea una tarjeta con texto motivacional"""
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(
                        ft.icons.CHECK_CIRCLE_ROUNDED,
                        color="white",
                        size=16,
                    ),
                    ft.Text(
                        text,
                        color="white",
                        size=14,
                        weight=ft.FontWeight.W_500,
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.symmetric(vertical=5),
            padding=ft.padding.all(10),
            border_radius=ft.border_radius.all(10),
            bgcolor=ft.colors.with_opacity(0.2, "white"),
        )