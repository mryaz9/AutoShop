from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from dialogs.admin.states import AdminMenu
from dialogs.assortiment.states import BotMenu
from filters.filters import is_admin
from lexicon.lexicon_ru import LEXICON_MAIN, LEXICON_BUTTON_MAIN


class MainMenu(StatesGroup):
    main_menu = State()


def main_menu_window():
    return Window(
        Const(LEXICON_MAIN["start"]),
        Start(Const(LEXICON_BUTTON_MAIN["assortment"]), id="assortment", state=BotMenu.select_categories),
        # Start(Const(LEXICON_BUTTON_MAIN["profile"]), id="profile", state=BannerSG.default),
        # Start(Const(LEXICON_BUTTON_MAIN["️orders"]), id="️orders", state=Product.show),
        # Start(Const(LEXICON_BUTTON_MAIN["information"]), id="information", state=Product.show),
        Start(Const("Администрирование"), id="admin", state=AdminMenu.admin_menu, when="admin"),
        state=MainMenu.main_menu,
        getter=is_admin
    )
