from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Cancel, Back
from aiogram_dialog.widgets.text import Const, Format

from dialogs import keyboard, getters
from dialogs.admin import selected, states
from lexicon.lexicon_ru import LEXICON_FSM_SHOP, LEXICON_MAIN


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
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.amount,
    )


def files_window():
    return Window(
        Const(LEXICON_FSM_SHOP["files"]),
        MessageInput(selected.on_chosen_files, [ContentType.TEXT, ContentType.DOCUMENT]),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.AddItem.files,
    )


def photo_window():
    return Window(
        Const(LEXICON_FSM_SHOP["photo"]),
        MessageInput(selected.on_chosen_photo, ContentType.PHOTO),
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
        Cancel(Const(LEXICON_MAIN["exit"])),
        state=states.AddItem.confirm,
        getter=getters.get_confirm_add
    )
