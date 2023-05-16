from aiogram import types
from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Cancel, Back, SwitchTo, Next, Button
from aiogram_dialog.widgets.text import Const, Format

from handlers import getters, keyboard
from handlers.admin import states
from handlers.admin import selected
from dictionary.dictionary_ru import LEXICON_ITEM as lex


def menu_window():
    return Window(
        Const(lex.get("item_menu")),
        SwitchTo(
            Const(lex.get("add_item")),
            state=states.AddItem.select_categories,
            id="add_item",
            on_click=selected.on_select_menu
        ),
        SwitchTo(
            Const(lex.get("hide_item")),
            state=states.AddItem.select_categories,
            id="hide_item",
            on_click=selected.on_select_menu
        ),
        Row(
            Cancel(Const(lex.get("to_menu")))
        ),
        state=states.AddItem.menu
    )


def categories_window():
    return Window(
        Const(lex.get("select_category")),
        keyboard.paginated_categories(selected.on_chosen_category),
        state=states.AddItem.select_categories,
        getter=getters.get_category
    )


def subcategories_window():
    return Window(
        Const(lex.get("select_subcategory")),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        state=states.AddItem.select_subcategories,
        getter=getters.get_subcategory
    )


def name_window():
    return Window(
        Const(lex.get("input_name")),
        MessageInput(selected.on_chosen_name, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("back_input_name"))),
        ),
        state=states.AddItem.name,
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
        state=states.AddItem.amount,
        getter=getters.item_files_getter,
    )


def photo_window():
    return Window(
        Const(lex.get("input_photo")),
        MessageInput(selected.on_chosen_photo, ContentType.PHOTO),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("back_input_photo"))),
        ),
        state=states.AddItem.photo,
    )


def price_window():
    return Window(
        Const(lex.get("input_price")),
        MessageInput(selected.on_chosen_price, ContentType.TEXT),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("back_input_price"))),
        ),
        state=states.AddItem.price,
    )


def description_window():
    return Window(
        Const(lex.get("input_description")),
        MessageInput(selected.on_chosen_description, ContentType.TEXT),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("back_input_description"))),
        ),
        state=states.AddItem.description,
    )


def confirm_window():
    return Window(
        Format(lex.get("confirm")),
        Row(
            Button(
                Const("Да"),
                id="confirm_yes",
                on_click=selected.on_chosen_confirm
            ),
            Row(
                Cancel(Const(lex.get("to_menu"))),
                Back(Const(lex.get("back_input_confirm"))),
            ),
        ),
        state=states.AddItem.confirm,
        getter=getters.get_confirm_add
    )


def hide_item_window():
    return Window(
        Const(lex.get("hide_item")),
        keyboard.paginated_product(selected.on_hide_item, hide=lambda d, w, m: True),
        state=states.AddItem.hide_item,
        getter=getters.get_product
    )

