from typing import Any

from aiogram.enums import ContentType
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, Window
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Url, Group, Cancel, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from loguru import logger

from lexicon.lexicon_ru import LEXICON_MAIN


class Payment(StatesGroup):
    payment_select = State()
    input_amount = State()
    payment_qiwi = State()
    successful = State()


def payment_select_window():
    return Window(
        Const("Выберите способ оплаты"),
        Group(
            SwitchTo(
                Const("Qiwi"),
                id="qiwi_pay",
                state=Payment.input_amount
            ),
            Row(
                Cancel(Const(LEXICON_MAIN["exit"]))
            )
        ),
        state=Payment.payment_select,
    )


def input_amount_window():
    return Window(
        Const("Введите сумму в руб."),
        MessageInput(
            func=on_input_amount, content_types=ContentType.TEXT
        ),
        state=Payment.input_amount
    )


async def on_input_amount(message: Message, message_input: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    if message.text.isdigit():
        ctx.dialog_data.update(amount=message.text)
    await manager.switch_to(Payment.payment_qiwi)


def payment_qiwi_window():
    return Window(
        Const("Оплатите"),
        Button(
            Const("Я оплатил"),
            id="check_payment",
        ),
        state=Payment.payment_qiwi
    )


def successful_window():
    return Window(
        Format("Успешно оплачено"),
        Button(
            Format("{item[-1]}"),
            id="successful_pay"
        ),
        state=Payment.successful,
    )

async def on_check_payment(callback: CallbackQuery, widget: Any, manager: DialogManager):
    pass


async def get_payment_qiwi(dialog_manager: DialogManager, **kwargs):
    pass

'''

p2p = QiwiP2PClient(secret_p2p=config.PRIVATE_TOKEN_QIWI)
@dp.callback_query_handler(lambda x: x.data and x.data.startswith("buy:"))
async def buy_callback(callback: types.CallbackQuery):
    replace = callback.data.replace("buy:", "")
    data_buy = await sql_read3(replace)
    global bill
    bill = await p2p.create_p2p_bill(amount=float(data_buy[1]), expire_at=datetime.now() + timedelta(minutes=30),
                                     pay_source_filter=["qw", "card", "mobile"])

    keyboard_buy = InlineKeyboardMarkup(row_width=1)
    keyboard_buy.add(InlineKeyboardButton(text="Ссылка для платежа", url=f"{bill.pay_url}"))
    keyboard_buy.add(InlineKeyboardButton(text="Я оплатил", callback_data=f"pay:{replace}"))
    keyboard_buy.add(InlineKeyboardButton(text="Отмена", callback_data=f"del_pay"))
    await callback.message.answer(text=f"Оплатите {data_buy[1]} рублей", reply_markup=keyboard_buy)
    await callback.answer()
    await callback.message.delete()


@dp.callback_query_handler(lambda x: x.data and x.data.startswith("pay:"))
async def buy_callback(callback: types.CallbackQuery):
    comment_in = callback.data.split(":")
    replace = comment_in[1]
    # Начинаем прием платежей
    if await p2p.check_if_bill_was_paid(bill):  # Проверяем статус
        data_buy = await sql_read3(replace)
        await callback.answer(text=f"Оплачено {data_buy[1]}руб.", show_alert=True)
        await callback.message.answer_photo(data_buy[4], f"Описание:\n{data_buy[3]}")
        await sql_delete_command(data_buy[0])
        await callback.answer()

    elif await p2p.check_if_bill_was_paid(bill) != True:
        await callback.answer(text=f"Платёж не получен!", show_alert=True)
'''