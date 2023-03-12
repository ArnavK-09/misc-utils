# imports
import flet as ft

class About(ft.UserControl):
    """
    About Page of site
    """
    # init

    def __init__(self, page):
        super().__init__()
        self.page = page

    # build
    def build(self):
        return ft.Container(
            padding=5,
            content=(ft.Text("About Us"))
        )
