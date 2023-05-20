from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel
from aiogram_dialog.widgets.text import Const

from handlers.admin.admin_menu.getter import getter_admins
from handlers.admin.admin_menu.state import Admin
from dictionary.dictionary_ru import LEXICON_ADMIN
from handlers.keyboard import paginated_admins


def menu_window():
    return Window(
        Const(LEXICON_ADMIN['admin_menu']),
        SwitchTo(
            Const(LEXICON_ADMIN['add_admin']),
            id="add_category",
            state=Admin.add_admin
        ),
        SwitchTo(
            Const(LEXICON_ADMIN['view_admin']),
            id="view_admin",
            state=Admin.view_admin
        ),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
        ),
        state=Admin.admin_menu
    )


def add_admin_window():
    return Window(
        Const(LEXICON_ADMIN['input_id_admin']),
        MessageInput(selected.on_add_admin, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
        ),
        state=Admin.add_admin,
    )


def view_admin_window():
    return Window(
        Const(LEXICON_ADMIN['select_admin']),
        paginated_admins(selected.on_del_admin),
        Row(
            Cancel(Const(LEXICON_ADMIN["to_menu"])),
        ),
        state=Admin.view_admin,
        getter=getter_admins
    )
