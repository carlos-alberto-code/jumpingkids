import flet as ft
# import flet_rive as ft_rive  # Comentado para evitar errores si no está instalado


class AnimationPanel(ft.Container):
    def __init__(self):
        super().__init__(
            width=500,
            bgcolor="#2D2242",
            border_radius=ft.border_radius.only(
                top_right=25, bottom_right=25
            ),
            padding=20,
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # Opción 2: Usando Lottie (incluido en flet)
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


class LoginForm(ft.Column):
    def __init__(self, on_login=None, on_switch_to_signup=None):
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400,
            controls=[
                ft.Text("JUMPINGKIDS", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Welcome back", size=16, color=ft.Colors.GREY_600),
                ft.Container(height=30),
                
                ft.TextField(
                    label="Email or username",
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.TextField(
                    label="Password",
                    password=True,
                    can_reveal_password=True,
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextButton(
                                text="Forgot password?", 
                                style=ft.ButtonStyle(color=ft.Colors.GREY_700)
                            ),
                        ]
                    ),
                    width=400,
                ),
                ft.Container(height=10),
                ft.ElevatedButton(
                    text="Log in",
                    width=400,
                    height=50,
                    on_click=on_login,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor="#2D2242",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Don't have an account?", color=ft.Colors.GREY_600),
                            ft.TextButton(
                                text="Sign up",
                                on_click=on_switch_to_signup,
                                style=ft.ButtonStyle(
                                    color="#2D2242",
                                )
                            )
                        ]
                    )
                )
            ]
        )


class SignupForm(ft.Column):
    def __init__(self, on_signup=None, on_switch_to_login=None):
        super().__init__(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400,
            controls=[
                ft.Text("JUMPINGKIDS", size=24, weight=ft.FontWeight.BOLD),
                ft.Text("Create an account", size=16, color=ft.Colors.GREY_600),
                ft.Container(height=30),
                
                ft.TextField(
                    label="Full Name",
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.TextField(
                    label="Email",
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.TextField(
                    label="Password",
                    password=True,
                    can_reveal_password=True,
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.TextField(
                    label="Confirm Password",
                    password=True,
                    can_reveal_password=True,
                    border_radius=8,
                    filled=True,
                    bgcolor=ft.Colors.GREY_100,
                    height=50,
                    width=400,
                ),
                ft.ElevatedButton(
                    text="Sign Up",
                    width=400,
                    height=50,
                    on_click=on_signup,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        bgcolor="#2D2242",
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                ),
                ft.Container(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Already have an account?", color=ft.Colors.GREY_600),
                            ft.TextButton(
                                text="Log in",
                                on_click=on_switch_to_login,
                                style=ft.ButtonStyle(
                                    color="#2D2242",
                                )
                            )
                        ]
                    )
                )
            ]
        )


class AuthPanel(ft.Container):
    def __init__(self, on_login=None, on_signup=None):
        super().__init__(
            expand=True,
            padding=ft.padding.all(40),
            animate=ft.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        
        # Crear los formularios
        self.login_form = LoginForm(
            on_login=on_login,
            on_switch_to_signup=lambda _: self.show_signup()
        )
        
        self.signup_form = SignupForm(
            on_signup=on_signup,
            on_switch_to_login=lambda _: self.show_login()
        )
        
        # Mostrar el formulario de login por defecto
        self.show_login()
    
    def show_login(self):
        self.content.controls = [self.login_form]
    
    def show_signup(self):
        self.content.controls = [self.signup_form]


class LoginView(ft.View):
    def __init__(self, on_login=None, on_signup=None):
        super().__init__(
            route="/login",
            padding=0,
            controls=[
                ft.Row(
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        AnimationPanel(),
                        AuthPanel(on_login=on_login, on_signup=on_signup),
                    ],
                    expand=True,
                )
            ],
        )


def main(page: ft.Page):
    page.title = "JumpingKids Login"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    def handle_login(e):
        # Aquí iría la lógica de autenticación
        print("Login attempt")
        # page.go("/home")  # Redirigir a la página principal después del login
    
    def handle_signup(e):
        # Aquí iría la lógica de registro
        print("Signup attempt")
        # page.go("/home")  # Redirigir a la página principal después del registro
    
    lv = LoginView(on_login=handle_login, on_signup=handle_signup)
    page.views.append(lv)
    page.go("/login")
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")