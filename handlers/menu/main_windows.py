from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.media import StaticMedia, DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from handlers.admin.states import AdminMenu
from handlers.menu.info_window import Info
from handlers.users.assortiment.states import BotMenu
from handlers.users.profile.states import Profile
from filters.filters import is_admin
from dictionary.dictionary_ru import LEXICON_MAIN


class MainMenu(StatesGroup):
    main_menu = State()


def main_menu_window():
    return Window(
        DynamicMedia("photo"),
        Format(LEXICON_MAIN.get("start").format(username="{event.from_user.username}")),
        Start(Const(LEXICON_MAIN.get("assortment")), id="assortment", state=BotMenu.select_categories),
        Start(Const(LEXICON_MAIN.get("profile")), id="profile", state=Profile.profile),
        Start(Const(LEXICON_MAIN.get("information")), id="information", state=Info.info),
        Start(Const(LEXICON_MAIN.get("admin")), id="admin", state=AdminMenu.admin_menu, when="admin"),
        state=MainMenu.main_menu,
        getter=is_admin
    )
