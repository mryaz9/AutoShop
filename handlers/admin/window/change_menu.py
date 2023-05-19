from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput, TextInput
from aiogram_dialog.widgets.kbd import Next, Row, Cancel, Back, Button
from aiogram_dialog.widgets.text import Const, Format

from dictionary.dictionary_ru import LEXICON_CHANGE_MENU
from handlers.admin import states, selected
from handlers.getters import change_menu_getter
from utils.custom_widget import PhotoInput


def input_photo_window(text: str, state, id_input):
    return Window(
        Const(text),
        PhotoInput(id=id_input, on_success=Next()),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_CHANGE_MENU.get("to_menu"))),
        ),
        state=state,
    )


def input_text_window(text: str, state, id_input):
    return Window(
        Const(text),
        TextInput(id=id_input, on_success=Next()),
        Next(Const("Пропустить")),
        Row(
            Cancel(Const(LEXICON_CHANGE_MENU.get("to_menu"))),
        ),
        state=state,
    )


def confirm_change_menu_window():
    return Window(
        Format("{change_menu}"),
        Button(
            Const("Добавить"),
            on_click=selected.confirm_change_menu,
            id="confirm_change_menu"),
        Row(
            Cancel(Const(LEXICON_CHANGE_MENU.get("to_menu"))),
        ),
        state=states.ChangeMenu.confirm,
        getter=change_menu_getter
    )
