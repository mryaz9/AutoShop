from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import SwitchTo, Row, Cancel, Back
from aiogram_dialog.widgets.text import Const

from dialogs.admin import states, selected
from lexicon.lexicon_ru import LEXICON_MAIN


def menu_window():
    return Window(
        Const("Рассылка"),
        SwitchTo(
            Const("Создать рассылку"),
            id="create_mailing",
            state=states.Mailing.create_mailing
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=states.Mailing.mailing_menu
    )


def create_mailing_window():
    return Window(
        Const("Введите сообщение рассылки"),
        MessageInput(selected.on_create_mailing, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Mailing.create_mailing
    )
