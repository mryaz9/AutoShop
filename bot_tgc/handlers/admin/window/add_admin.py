from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel
from aiogram_dialog.widgets.text import Const

from bot_tgc.dictionary.dictionary_ru import LEXICON_ADMIN
from bot_tgc.handlers import getters
from bot_tgc.handlers.admin import selected, states
from bot_tgc.handlers.keyboard import paginated_admins


def menu_window():
    return Window(
        Const(LEXICON_ADMIN['admin_menu']),
        SwitchTo(
            Const(LEXICON_ADMIN['add_admin']),
            id="add_category",
            state=states.AddAdmin.add_admin
        ),
        SwitchTo(
            Const(LEXICON_ADMIN['view_admin']),
            id="view_admin",
            state=states.AddAdmin.view_admin
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
        ),
        state=states.AddAdmin.add_admin,
    )


def view_admin_window():
    return Window(
        Const(LEXICON_ADMIN['select_admin']),
        paginated_admins(selected.on_del_admin),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
        ),
        state=states.AddAdmin.view_admin,
        getter=getters.getter_admins
    )
