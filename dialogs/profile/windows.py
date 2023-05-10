from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row, Back
from aiogram_dialog.widgets.text import Const

from dialogs.profile.states import Profile
from lexicon.lexicon_ru import LEXICON_MAIN


def profile_window():
    return Window(
        Const("Профиль:"),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=Profile.profile
    )


def orders_window():
    return Window(
        Const("Заказы:"),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=Profile.profile
    )
