from aiogram_dialog import Dialog

from dictionary.dictionary_ru import LEXICON_CHANGE_MENU
from handlers.admin.change_menu.state import ChangeMenu
from handlers.admin.change_menu.window import confirm_change_menu_window
from utils.widget import input_photo_window, input_text_window


def change_menu_dialogs():
    return [
        Dialog(
            input_photo_window(
                text=LEXICON_CHANGE_MENU.get("main_menu"),
                state=ChangeMenu.main_menu,
                id_input="main_menu"
            ),
            input_photo_window(
                text=LEXICON_CHANGE_MENU.get("catalog"),
                state=ChangeMenu.catalog,
                id_input="catalog"
            ),
            input_photo_window(
                text=LEXICON_CHANGE_MENU.get("order"),
                state=ChangeMenu.order,
                id_input="order"
            ),
            input_photo_window(
                text=LEXICON_CHANGE_MENU.get("profile"),
                state=ChangeMenu.profile,
                id_input="profile"
            ),
            input_photo_window(
                text=LEXICON_CHANGE_MENU.get("info"),
                state=ChangeMenu.info,
                id_input="info"
            ),
            input_text_window(
                text=LEXICON_CHANGE_MENU.get("info_about"),
                state=ChangeMenu.info_about,
                id_input="info_about"
            ),
            confirm_change_menu_window()
        )
    ]
