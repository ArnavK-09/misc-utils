# imports
import flet as ft


class UtilCard(ft.UserControl):
    """
    UtilCard - component for showing info about utilities
    """

    def __init__(self, title: str = "Title", description: str = "Description", icon=ft.icons.TEXT_SNIPPET, id: str = "/"):
        super().__init__()
        self.title = title
        self.icon = icon
        self.util_route = id
        self.description = description

    def build(self):
        return ft.Card(
            content=ft.Container(
                # on_click=go_to_util_page,
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(
                                self.icon if self.icon else ft.icons.TEXT_SNIPPET),
                            title=ft.Text(self.title),
                            subtitle=ft.Text(
                                self.description
                            ),
                        ),
                        ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Use", color="black", bgcolor="white",
                                )],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=8,
            )
        )
