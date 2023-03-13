# imports 
import flet as ft
from utilities import text_count

# all utils index
UTILS_LIST = [
    {
        "name": "Text Counter",
        "description": "Count letters, words & chracters of your text",
        "id": "text_count",
        "icon": ft.icons.ABC,
        "page": text_count
    },
    {
        "name": "Click Counter",
        "description": "Count the clicks",
        "id": "click_count"
    }
]
