from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel, Back
from aiogram_dialog.widgets.text import Const

from dialogs.admin import states, selected
from lexicon.lexicon_ru import LEXICON_ADMIN


def menu_window():
    return Window(
        Const(LEXICON_ADMIN['admin_menu']),
        SwitchTo(
            Const(LEXICON_ADMIN['add_admin']),
            id="add_category",
            state=states.AddAdmin.add_admin
        ),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
        ),
        state=states.AddAdmin.admin_menu
    )


def add_admin_window():
    return Window(
        Const(LEXICON_ADMIN['input_id_admin']),
        MessageInput(selected.on_add_admin, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
            Back(Const(LEXICON_ADMIN["to_admin_menu"])),
        ),
        state=states.AddAdmin.add_admin,
    )

