import operator

from aiogram.enums import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Row, Button, Cancel, SwitchTo, Back, Url, Select
from aiogram_dialog.widgets.text import Const, Format

from filters.filters import is_admin
from dictionary.dictionary_ru import LEXICON_PAYMENT as lex
from handlers.admin import on_select_menu
from payment import states, getters, selected


def payment_select_window():
    return Window(
        Const(lex.get("payment_menu")),
        SwitchTo(
            Const(lex.get("qiwi")),
            id="qiwi_select",
            state=states.Payment.payment_input_amount,
            on_click=on_select_menu
        ),
        SwitchTo(
            Const(lex.get("crypto")),
            id="crypto_select",
            state=states.Payment.payment_input_amount,
            on_click=on_select_menu
        ),
        SwitchTo(
            Const(lex.get("admin")),
            id="admin_select",
            state=states.Payment.payment_input_amount,
            on_click=on_select_menu,
            when="admin"
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
        ),
        state=states.Payment.payment_select,
        getter=is_admin
    )


def input_amount_window():
    return Window(
        Const(lex.get("input_amount")),
        MessageInput(
            selected.on_input_amount,
            content_types=ContentType.TEXT
        ),
        Row(
            Cancel(Const(lex.get("to_menu"))),
            Back(Const(lex.get("to_payment_menu"))),
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
                Const(lex.get("to_menu")),
                on_click=selected.on_reject_qiwi_payment
            ),
            Back(
                Const(lex.get("back_input_amount")),
                on_click=selected.on_reject_qiwi_payment
            ),
        ),
        state=states.Payment.payment_qiwi,
        getter=getters.get_payment_qiwi
    )


def select_assets_window():
    return Window(
        Const(lex.get("select_assets")),
        Select(
            Format(
                '{item[0]}'
            ),
            id="s_asset",
            item_id_getter=operator.itemgetter(1),
            items="assets",
            on_click=selected.on_select_asset,
        ),
        Row(
            Cancel(Const(lex.get("to_menu")),),
            Back(Const(lex.get("back_input_amount"))),
        ),
        state=states.Payment.payment_select_assets,
        getter=getters.get_assets_crypto
    )


def payment_crypto_window():
    return Window(
        Format("Оплатите {amount} {asset}"),
        Url(
            Const("Ссылка для оплаты"),
            url=Format("{bill_url}"),
        ),
        Button(
            Const("Я оплатил"),
            id="crypto_pay_check",
            on_click=selected.on_check_crypto_payment
        ),
        Row(
            Cancel(Const(lex.get("to_menu")), ),
            Back(Const(lex.get("select_assets"))),
        ),
        state=states.Payment.payment_crypto,
        getter=getters.get_payment_crypto
    )

