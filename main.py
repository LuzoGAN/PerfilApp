import flet as ft

# Style do link como dicionanrio
link_style: dict[str, Any] = {
    'height': 50,
    'focused_border_color': '#F4CE14',
    'border_radius':5,
    'cursor_height':16,
    'cursor_color': 'white',
    'content_paddind':10,
    'border_width':1.5,
    'text_size': 14,
    'label_style': ft.TextStyle(color='#F4CE14'),
}

# Definindo o link como class
class Link(ft.TextField):
    def __init__(self, label: str, value: str, page: ft.Page):
        super().__init__(
            value=value,
            read_only=True,
            label=label,
            on_focus=None,
            **link_style
        )


# Perfil
class ProfilePage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route='/profile', padding=20),

        self.page: Page = page

        self.controls: list[SafeArea] = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    horizontal_alignment='center',
                    controls=[
                        ft.Divider(height=20, color='transparent'),
                        ft.Container(
                            bgcolor='white10',
                            width=128,
                            height=128,
                            shape=ft.BoxShape('circle'),
                            # Image do Perfil
                            image_src='/perfil.jpg',
                            image_fit='cover',
                            shadow=ft.BoxShadow(
                                spread_radius=6,
                                blur_radius=20,
                                color=ft.colors.with_opacity(0.71, 'black'),
                            )
                        ),
                        ft.Divider(height=10, color='transparent'),
                        ft.Text('Luzo Gomes', size=32),
                        ft.Text(
                            'Python Programming',
                            weight='w400',
                            text_align='center'
                        ),
                        ft.Divider(height=50, color='transparent'),
                        ft.Column(
                            spacing=20,
                            controls=[
                                Link('Nome', 'Luzo Gomes', self.page),
                                Link('Youtube', '@Luzo', self.page)
                                #inserir link aqui ...
                            ]
                        )
                    ]
                )
            )
        ]


# Definindo pagina de carregamento
class LandingPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route='/landing', padding=60)

        self.page = page

        # Definindo a var lock icone
        self.lock = ft.Icon(
            name='lock', scale=ft.Scale(4)
        )

        # Definindo o butão para voltar ao perfil
        self.button = ft.Container(
            border_radius=5,
            expand=True,
            bgcolor='#F4CE14',
            content=ft.Text('Olhe o Link', color='black', size=18),
            padding=ft.padding.only(left=25, right=25, top=10, bottom=10),
            alignment=ft.alignment.center,
            on_click=None
        )

        # Definindo a lista de controles para a view
        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    alignment='spaceBetween',
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Divider(height=120,
                                           color='transparent'),
                                self.lock,
                                ft.Divider(height=70, color='transparent'),
                                ft.Text(
                                    'Link  para verificar',
                                    size=18,
                                    text_align='center'
                                )
                                ],
                            horizontal_alignment='center'
                        ),
                        ft.Row(
                            controls=[self.button],
                            alignment='center'
                        )
                    ],
                )
            )
        ]

def main(page: ft.Page):
    # Tema
    page.theme_mode = ft.ThemeMode.DARK

    # Definindo o metodo para o aperto entre os routing
    def router(route):
        page.views.clear()

        if page.route == '/landing':
            landing = LandingPage(page)
            page.views.append(landing)

        if page.route == '/profile':
            profile = ProfilePage(page)
            page.views.append(profile)

        page.update()

    page.on_route_change = router
    page.go('/profile')

    page.update()


ft.app(target=main, assets_dir='assets')