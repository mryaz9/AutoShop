from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from dialogs.admin import selected, keyboard, states, getters

from lexicon.lexicon_ru import LEXICON_INLINE_MENU


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        # Cancel(Const(LEXICON_MAIN["back"])),
        state=states.AdminMenu.select_categories,
        getter=getters.get_categories
    )


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        state=states.AdminMenu.select_subcategories,
        getter=getters.get_subcategories
    )


def product_window():
    return Window(
        Const(LEXICON_INLINE_MENU["name"]),
        keyboard.paginated_product(selected.on_chosen_product),
        state=states.AdminMenu.select_product,
        getter=getters.get_product
    )
