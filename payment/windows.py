from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Button, Cancel, SwitchTo, Back, Url
from aiogram_dialog.widgets.text import Const, Format

from lexicon.lexicon_ru import LEXICON_MAIN
from payment import states, getters, selected


def payment_select_window():
    return Window(
        Const("Выберите способ оплаты"),
        SwitchTo(
            Const("qiwi"),
            id="qiwi_select",
            state=states.Payment.payment_input_amount
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
        ),
        state=states.Payment.payment_select,
    )


def input_amount_window():
    return Window(
        Const("Введите сумму"),
        MessageInput(
            selected.on_input_amount,
            content_types=ContentType.TEXT
        ),
        Row(
            Cancel(Const(LEXICON_MAIN["exit"])),
            Back(Const(LEXICON_MAIN["back"])),
        ),
        state=states.Payment.payment_input_amount,
    )


def payment_qiwi_window():
    return Window(
        Format("Оплатите {amount}руб."),
        Url(
            Const("Ссылка для оплаты"),
            url=Format("{bill_url}"),
        ),
        Button(
            Const("Я оплатил"),
            id="qiwi_pay_check",
            on_click=selected.on_check_qiwi_payment
        ),
        Row(
            Cancel(
                Const(LEXICON_MAIN["exit"]),
                on_click=selected.on_reject_qiwi_payment
            ),
            Back(
                Const(LEXICON_MAIN["back"]),
                on_click=selected.on_reject_qiwi_payment
            ),
        ),
        state=states.Payment.payment_qiwi,
        getter=getters.get_payment_qiwi
    )
