from aiogram import types
from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Row, Cancel, Back, SwitchTo, Next, Button
from aiogram_dialog.widgets.text import Const, Format

from handlers import getters, keyboard
from handlers.admin.item_menu.state import Item
from handlers.admin.menu import states
from handlers.admin import selected
from dictionary.dictionary_ru import LEXICON_ITEM as lex
from utils.custom_widget import PhotoInput


def menu_window():
    return Window(
        Const(lex.get("item_menu")),
        SwitchTo(
            Const(lex.get("add_item")),
            state=Item.select_categories,
            id="add_item",
            on_click=selected.on_select_menu
        ),
        SwitchTo(
            Const(lex.get("add_files")),
            state=Item.select_categories,
            id="add_files",
            on_click=selected.on_select_menu
        ),
        SwitchTo(
            Const(lex.get("del_item")),
            state=Item.select_categories,
            id="del_item",
            on_click=selected.on_select_menu
        ),
        Row(
            Cancel(Const(lex.get("to_menu")))
        ),
        state=Item.menu
    )


def categories_window():
    return Window(
        Const(lex.get("select_category")),
        keyboard.paginated_categories(selected.on_chosen_category),
        state=Item.select_categories,
        getter=getters.getter_category
    )


def subcategories_window():
    return Window(
        Const(lex.get("select_subcategory")),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        state=Item.select_subcategories,
        getter=getters.getter_subcategory
    )


def items_window():
    return Window(
        Const(lex.get("select_item")),
        keyboard.paginated_product(selected.on_chosen_items),
        state=Item.select_item,
        getter=getters.getter_product
    )


def add_files_window():
    return Window(
        Const(lex.get("input_amount")),
        Format("Получено {files_count} файлов", when="files_count"),
        MessageInput(selected.on_chosen_amount, content_types=types.ContentType.DOCUMENT),
        SwitchTo(
            Const("Далее"),
            id="sw_t_add_files",
            state=Item.confirm_add_files,
            when="files_count"
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const("Назад")),
        ),
        state=Item.add_files,
        getter=getters.item_files_getter,
    )


def amount_window():
    return Window(
        Const(lex.get("input_amount")),
        Format("Получено {files_count} файлов", when="files_count"),
        MessageInput(selected.on_chosen_amount, content_types=types.ContentType.DOCUMENT),
        Next(Const("Далее")),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("back_input_amount"))),
        ),
        state=Item.amount,
        getter=getters.item_files_getter,
    )
