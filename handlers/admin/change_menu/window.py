from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Cancel, Button
from aiogram_dialog.widgets.text import Const, Format

from dictionary.dictionary_ru import LEXICON_CHANGE_MENU
from handlers.admin.change_menu.getter import change_menu_getter
from handlers.admin.change_menu.selected import confirm_change_menu
from handlers.admin.change_menu.state import ChangeMenu


def confirm_change_menu_window():
    return Window(
        Format("{change_menu}"),
        Button(
            Const("Добавить"),
            on_click=confirm_change_menu,
            id="confirm_change_menu"),
        Row(
            Cancel(Const(LEXICON_CHANGE_MENU.get("to_menu"))),
        ),
        state=ChangeMenu.confirm,
        getter=change_menu_getter
    )
