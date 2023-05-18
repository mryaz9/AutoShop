from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from handlers.admin.states import AdminMenu
from handlers.users.assortiment.states import BotMenu
from handlers.users.profile.states import Profile
from filters.filters import is_admin
from dictionary.dictionary_ru import LEXICON_MAIN


class MainMenu(StatesGroup):
    main_menu = State()


def main_menu_window():
    return Window(
        Const(LEXICON_MAIN.get("start")),
        Start(Const(LEXICON_MAIN.get("assortment")), id="assortment", state=BotMenu.select_categories),
        Start(Const(LEXICON_MAIN.get("profile")), id="profile", state=Profile.profile),
        # Start(Const(LEXICON_BUTTON_MAIN["information"]), id="information", state=Product.show),
        Start(Const(LEXICON_MAIN.get("admin")), id="admin", state=AdminMenu.admin_menu, when="admin"),
        state=MainMenu.main_menu,
        getter=is_admin
    )
