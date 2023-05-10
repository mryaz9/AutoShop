from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Cancel, Back, SwitchTo, Radio, Next
from aiogram_dialog.widgets.text import Const, Format

from dialogs import keyboard, getters
from dialogs.admin import selected, states
from lexicon.lexicon_ru import LEXICON_FSM_SHOP, LEXICON_MAIN, LEXICON_INLINE_MENU


def categories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["category"]),
        keyboard.paginated_categories(selected.on_chosen_category),
        state=states.AddItem.select_categories,
        getter=getters.get_categories
    )


def subcategories_window():
    return Window(
        Const(LEXICON_INLINE_MENU["subcategory"]),
        keyboard.paginated_subcategories(selected.on_chosen_subcategories),
        state=states.AddItem.select_subcategories,
        getter=getters.get_subcategories
    )


def name_window():
    return Window(
        Const(LEXICON_FSM_SHOP["name"]),
        MessageInput(selected.on_chosen_name, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.name,
    )


def amount_window():
    return Window(
        Const(LEXICON_FSM_SHOP["amount"]),
        MessageInput(selected.on_chosen_amount, ContentType.TEXT),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.amount,
    )


def photo_window():
    return Window(
        Const(LEXICON_FSM_SHOP["photo"]),
        MessageInput(selected.on_chosen_photo, ContentType.PHOTO),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.photo,
    )


def price_window():
    return Window(
        Const(LEXICON_FSM_SHOP["price"]),
        MessageInput(selected.on_chosen_price, ContentType.TEXT),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.price,
    )


def time_action_window():
    return Window(
        Const(LEXICON_FSM_SHOP["time_action"]),
        MessageInput(selected.on_chosen_time_action, ContentType.TEXT),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.time_action,
    )


def description_window():
    return Window(
        Const(LEXICON_FSM_SHOP["description"]),
        MessageInput(selected.on_chosen_description, ContentType.TEXT),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.description,
    )


def confirm_window():
    return Window(
        Const("Все правильно?"),
        Format(LEXICON_FSM_SHOP["done_2"]),
        keyboard.confirm_kb(selected.on_chosen_confirm),
        state=states.AddItem.confirm,
        getter=getters.get_confirm_add
    )
