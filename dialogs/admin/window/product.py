from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row, Cancel, Back
from aiogram_dialog.widgets.text import Const

from dialogs import keyboard, getters
from dialogs.admin import selected, states
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_MAIN


def product_window():
    return Window(
        Const(LEXICON_INLINE_MENU["name"]),
        #keyboard.paginated_product(selected.on_chosen_product),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Product.select_product,
        getter=getters.get_product
    )