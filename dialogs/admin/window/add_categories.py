from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Back, Row
from aiogram_dialog.widgets.text import Const

from dialogs import keyboard, getters
from dialogs.admin import states, selected
from lexicon.lexicon_ru import LEXICON_INLINE_MENU, LEXICON_MAIN, LEXICON_FSM_SHOP


def menu_window():
    return Window(
        Const("Редактирование категорий"),
        SwitchTo(
            Const("Добавить категорию"),
            id="add_category",
            state=states.AddCategories.add_categories
        ),
        SwitchTo(
            Const("Добавить подкатегорию"),
            id="add_subcategory",
            state=states.AddCategories.select_categories
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=states.AddCategories.categories_menu
    )


def select_categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_select_add_category),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddCategories.select_categories,
        getter=getters.get_categories
    )


def add_categories_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_category_name"]),
        MessageInput(selected.on_add_category, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddCategories.add_categories,
    )


def add_subcategories_window():
    return Window(
        Const(LEXICON_FSM_SHOP["new_subcategory_name"]),
        MessageInput(selected.on_add_subcategory, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddCategories.add_subcategories,
    )

