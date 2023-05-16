import asyncio
import logging
from typing import Any

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ContentType
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, Window, Dialog, setup_dialogs, StartMode
from aiogram_dialog.widgets.input import TextInput, MessageInput
from aiogram_dialog.widgets.kbd import Button, Url, Group, Cancel, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from loguru import logger

from dictionary.dictionary_ru import LEXICON_MAIN


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


def payment_dialogs():
    return [
        Dialog(
            payment_select_window(),
            input_amount_window(),
            payment_qiwi_window(),
            successful_window()
        )
    ]


router = Router()


@router.message(CommandStart())
async def user_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(Payment.payment_select, mode=StartMode.RESET_STACK)


async def main():
    storage = MemoryStorage()
    bot: Bot = Bot(token="789267899:AAE7YbObi6q2v1uiu2H3f7qZ8RIq9UYDLlY")
    dp: Dispatcher = Dispatcher(storage=storage)

    for dialog in payment_dialogs():
        dp.include_router(dialog)

    setup_dialogs(dp)

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
