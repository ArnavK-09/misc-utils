# imports
import flet as ft
from views import views_handler


def main(page: ft.Page):

    # route handler
    def handle_route(_):
        """
          Matches the given route with view_handler
        """

        page.views.clear()
        try:
            page.views.append(
                views_handler(page)[page.route]
            )
        except:
            page.views.append(
                views_handler(page)['/']
            )
            
    # customizations
    page.window_bgcolor = ft.colors.BLACK
    page.bgcolor = ft.colors.BLACK

    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]
    appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Trolli",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
    )
    page.appbar = appbar
    page.update()

    # on route change
    page.on_route_change = handle_route
    # land on index page
    page.go('/')


# start
ft.app(target=main, view=ft.WEB_BROWSER)
