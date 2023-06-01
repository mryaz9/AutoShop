from aiogram.fsm.state import StatesGroup, State
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Row
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Format, Const

from bot_tgc.dictionary.dictionary_ru import LEXICON_PROFILE
from bot_tgc.handlers.getters import getter_info


class Info(StatesGroup):
    info = State()


def info_window():
    return Window(
        DynamicMedia("photo"),
        Format("{info}"),
        Row(
            Cancel(Const(LEXICON_PROFILE.get("to_menu"))),
        ),
        state=Info.info,
        getter=getter_info
    )
