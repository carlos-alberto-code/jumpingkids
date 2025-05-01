import flet as ft

class WelcomeComponent(ft.Container):
    
    def __init__(self, username):
        self.username = username
        
        content = ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text(
                        f"¡Hola, {username}!", 
                        size=26, 
                        weight=ft.FontWeight.BOLD, 
                        color="#7C4DFF"  # Morado principal
                    ),
                    ft.Text(
                        "¿Listo para divertirte ejercitándote hoy?", 
                        size=16, 
                        color="#3E2723",  # Texto café oscuro
                        weight=ft.FontWeight.W_400
                    ),
                ], expand=True),
                ft.Container(
                    content=ft.Lottie(
                        "https://assets5.lottiefiles.com/packages/lf20_touohxv0.json",
                        width=100,
                        height=100,
                        repeat=True,
                        animate=True
                    ),
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=10, bottom=20),
                )
            ]),
        ])
        
        # Inicializar el contenedor con los estilos adecuados
        super().__init__(
            content=content,
            padding=20,
            border_radius=16,
            bgcolor="white",
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.with_opacity(0.2, "grey")
            ),
        )
