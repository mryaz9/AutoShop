from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, Cancel, Back, SwitchTo
from aiogram_dialog.widgets.text import Const

from dialogs import keyboard, getters
from dialogs.admin import selected, states
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_FSM_SHOP, LEXICON_MAIN


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        SwitchTo(Const(
            LEXICON_FSM_SHOP["add_new_category"]), id="add_new_subcategory", state=states.SubCategory.add_subcategories
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.SubCategory.select_subcategories,
        getter=getters.get_subcategories
    )


def add_subcategories_name_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_subcategory_name"]),
        MessageInput(selected.on_add_new_subcategory_name, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.SubCategory.add_subcategories,
    )

