from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Back, Row
from aiogram_dialog.widgets.text import Const

from dialogs import keyboard, getters
from dialogs.admin import states, selected
from lexicon.lexicon_ru import LEXICON_CATEGORIES as lex


def menu_window():
    return Window(
        Const(lex.get("categories_menu")),
        SwitchTo(
            Const(lex.get("add_categories")),
            id="add_category",
            state=states.AddCategories.add_categories
        ),
        SwitchTo(
            Const(lex.get("add_subcategories")),
            id="add_subcategory",
            state=states.AddCategories.select_categories
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
        ),
        state=states.AddCategories.categories_menu
    )


def select_categories_window():
    return Window(
        Const(lex.get("select_category")),
        keyboard.paginated_categories(selected.on_select_add_category),
        state=states.AddCategories.select_categories,
        getter=getters.get_categories
    )


def add_categories_window():
    return Window(
        Const(lex.get("input_new_category")),
        MessageInput(selected.on_add_category, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("to_category_menu"))),
        ),
        state=states.AddCategories.add_categories,
    )


def add_subcategories_window():
    return Window(
        Const(lex.get("new_subcategory_name")),
        MessageInput(selected.on_add_subcategory, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("exit"))),
            Back(Const(lex.get("back"))),
        ),
        state=states.AddCategories.add_subcategories,
    )

