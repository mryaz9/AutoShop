from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from glQiwiApi import QiwiP2PClient
from loguru import logger

from config.config import load_config, Config
from database.models import Users
from payment import states, init_qiwi_client


async def on_input_amount(message: Message, message_input: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(amount=message.text)
    await manager.switch_to(states.Payment.payment_qiwi)


async def on_check_qiwi_payment(callback: CallbackQuery, button: Button, manager: DialogManager):
    ctx = manager.current_context()
    bill_id = ctx.dialog_data.get("bill_id")

    p2p = init_qiwi_client()

    status = await p2p.get_bill_status(bill_id)

    await p2p.close()

    if status == "PAID":
        await callback.answer("Платеж прошел успешно")

        user = Users()
        balance = user.balance
        user.balance += balance
        await user.create()

        await manager.done()

    else:
        await callback.answer("Платеж пока не получен")


async def on_reject_qiwi_payment(callback: CallbackQuery, button: Button, manager: DialogManager):
    ctx = manager.current_context()
    bill_id = ctx.dialog_data.get("bill_id")

    p2p = init_qiwi_client()

    await p2p.reject_p2p_bill(bill_id)

    await p2p.close()

    await callback.answer("Платеж отменен")
