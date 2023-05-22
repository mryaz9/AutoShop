from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel, Back
from aiogram_dialog.widgets.text import Const

from dictionary.dictionary_ru import LEXICON_MAILING as lex
from handlers.admin import selected
from handlers.admin import states


def menu_window():
    return Window(
        Const(lex.get("item_menu")),
        SwitchTo(
            Const(lex.get("create_mailing")),
            id="create_mailing",
            state=states.Mailing.create_mailing
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
        ),
        state=states.Mailing.mailing_menu
    )


def create_mailing_window():
    return Window(
        Const("Введите сообщение рассылки"),
        MessageInput(selected.on_create_mailing, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("to_mailing_menu"))),
        ),
        state=states.Mailing.create_mailing
    )
