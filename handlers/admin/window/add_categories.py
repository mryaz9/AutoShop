from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Back, Row, Button
from aiogram_dialog.widgets.text import Const

from handlers import getters, keyboard
from handlers.admin import states
from handlers.admin import selected
from dictionary.dictionary_ru import LEXICON_CATEGORIES as lex
from handlers.admin.selected import on_select_menu


def menu_window():
    return Window(
        Const(lex.get("categories_menu")),
        SwitchTo(
            Const(lex.get("add_categories")),
            id="add_category",
            state=states.AddCategories.add_categories,
            on_click=on_select_menu
        ),
        SwitchTo(
            Const(lex.get("add_subcategories")),
            id="add_subcategory",
            state=states.AddCategories.select_categories,
            on_click=on_select_menu
        ),
        SwitchTo(
            Const(lex.get("del_categories")),
            id="del_categories",
            state=states.AddCategories.select_categories,
            on_click=on_select_menu
        ),
        SwitchTo(
            Const(lex.get("del_subcategories")),
            id="del_subcategories",
            state=states.AddCategories.select_categories,
            on_click=on_select_menu
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
        ),
        state=states.AddCategories.categories_menu
    )


def select_categories_window():
    return Window(
        Const(lex.get("select_category")),
        keyboard.paginated_categories(selected.on_select_category),
        state=states.AddCategories.select_categories,
        getter=getters.get_category
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
        Const(lex.get("input_new_subcategory")),
        MessageInput(selected.on_add_subcategory, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("to_category_menu"))),
        ),
        state=states.AddCategories.add_subcategories,
    )


def select_subcategories_window():
    return Window(
        Const(lex.get("select_subcategory")),
        keyboard.paginated_subcategories(selected.on_select_subcategory),
        state=states.AddCategories.select_subcategories,
        getter=getters.get_subcategory
    )


def del_subcategories_confirm_window():
    return Window(
        Const(lex.get("del_subcategories_confirm")),
        Button(
            Const(
                "Да"
            ),
            id="del_subcategories",
            on_click=selected.on_del_subcategories
        ),
        Back(Const(lex.get("back_del_subcategories_confirm"))),
        state=states.AddCategories.del_subcategories,
    )


def del_categories_confirm_window():
    return Window(
        Const(lex.get("del_categories_confirm")),
        Button(
            Const(
                "Да"
            ),
            id="del_categories",
            on_click=selected.on_del_categories
        ),
        Back(Const(lex.get("back_del_categories_confirm"))),
        state=states.AddCategories.del_categories,
    )

