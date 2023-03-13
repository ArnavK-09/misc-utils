# imports
import flet as ft
from data.utilities import UTILS_LIST
from components.UtilCard import UtilCard

# all cards
cards = []

for util in UTILS_LIST:
    cards.append(
        ft.Container(
            UtilCard(util.get("name"), util.get("description"),
                     util.get("icon"), util.get("id")),
            col={"sm": 1, "md": 2, "xl": 3}
        )
    )


class Home(ft.UserControl):
    """
    Home Page of site listing all text utils
    """
    # init

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.utils = UTILS_LIST

    # build
    def build(self):
        return ft.Container(
            padding=5,
            content=(ft.ResponsiveRow(cards))
        )
