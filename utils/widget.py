from typing import Union, Awaitable

from aiogram.fsm.state import State
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Next, Row, Cancel, Back, Button
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.widget_event import WidgetEventProcessor

from dictionary.dictionary_ru import BUTTON_MENU
from utils.custom_widget import PhotoInput


def input_photo_window(text: str, state: State, id_input: str, when: bool,
                       on_success: Union[Awaitable | WidgetEventProcessor | None] = Next()) -> Window:
    return Window(
        Const(text),
        PhotoInput(id=id_input, on_success=on_success),
        Next(Const("Пропустить")) if when else None,
        Row(
            Cancel(Const(BUTTON_MENU.get("to_menu"))),
            Back(Const(BUTTON_MENU.get("back"))),
        ),
        state=state,
    )


def input_text_window(text: str, state: State, id_input: str, when: bool,
                      on_success: Union[Awaitable | WidgetEventProcessor | None] = Next()) -> Window:
    return Window(
        Const(text),
        TextInput(id=id_input, on_success=on_success),
        Next(Const("Пропустить")) if when else None,
        Row(
            Cancel(Const(BUTTON_MENU.get("to_menu"))),
            Back(Const(BUTTON_MENU.get("back"))),
        ),
        state=state,
    )


def confirm_window(text: str, state: State, id_confirm: str,
                   on_click: Union[Awaitable | WidgetEventProcessor | None])\
        -> Window:

    return Window(
        Format(text),
        Button(
            Const("Да"),
            id=id_confirm,
            on_click=on_click
        ),
        Row(
            Cancel(Const(BUTTON_MENU.get("to_menu"))),
            Back(Const(BUTTON_MENU.get("back"))),
        ),
        state=state,
    )
