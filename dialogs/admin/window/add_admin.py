from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel
from aiogram_dialog.widgets.text import Const

from dialogs.admin import states, selected
from lexicon.lexicon_ru import LEXICON_MAIN


def menu_window():
    return Window(
        Const("Редактирование админов"),
        SwitchTo(
            Const("Добавить админа"),
            id="add_category",
            state=states.AddAdmin.add_admin
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=states.AddAdmin.admin_menu
    )


def add_admin_window():
    return Window(
        Const("Введите id"),
        MessageInput(selected.on_add_admin, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=states.AddAdmin.add_admin,
    )

