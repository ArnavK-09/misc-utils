# imports
from flet import *
from pages.home import Home
from pages.about import About
from data.utilities import UTILS_LIST


def views_handler(page):
    """
    Views handler for site pages
    """
    return {
        '/': View(
            route='/',
            controls=[
                Home(page)
            ]
        ),
        '/about': View(
            route='/about',
            controls=[
                About(page)
            ]
        ),

        # test
        '/utilities/text_Count': View(
            route='/utilities/text_Count',
            controls=[
               About(page)
            ]
        ),
    }
