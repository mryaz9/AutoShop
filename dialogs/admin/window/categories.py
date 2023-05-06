from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, Back, SwitchTo
from aiogram_dialog.widgets.text import Const

from dialogs import getters
from dialogs.admin import selected, states, keyboard
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_FSM_SHOP, LEXICON_MAIN


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        Cancel(Const(LEXICON_MAIN["back"])),
        state=states.Category.select_categories,
        getter=getters.get_categories
    )


def add_categories_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_category_name"]),
        MessageInput(selected.on_add_new_category_name, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Category.add_categories,
    )
