from typing import Any

from aiocryptopay.const import Assets, InvoiceStatus
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.user import get_user, add_balance
from database.models import Users
from payment import states
from utils.init_payment import init_qiwi_client, init_crypto_client


async def on_input_amount(message: Message, message_input: MessageInput, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    ctx.dialog_data.update(amount=int(message.text))
    menu = ctx.dialog_data.get("menu")

    if menu == "qiwi_select":
        await manager.switch_to(states.Payment.payment_qiwi)

    elif menu == "crypto_select":
        await manager.switch_to(states.Payment.payment_select_assets)

    elif menu == "admin_select":
        await add_balance(session, float(int(message.text)), message.from_user.id)
        await manager.done()


async def on_select_asset(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(asset=item_id)
    await manager.switch_to(states.Payment.payment_crypto)


async def on_check_qiwi_payment(callback: CallbackQuery, button: Button, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    bill_id = ctx.dialog_data.get("bill_id")
    amount = ctx.dialog_data.get("amount")

    p2p = init_qiwi_client()

    status = await p2p.get_bill_status(bill_id)

    await p2p.close()

    if status == "PAID":
        await callback.answer("Платеж прошел успешно")

        await add_balance(session, float(amount), callback.from_user.id)

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


async def on_check_crypto_payment(callback: CallbackQuery, button: Button, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    bill_id = ctx.dialog_data.get("bill_id")
    amount = ctx.dialog_data.get("amount")

    crypto = init_crypto_client()

    status = await crypto.get_invoices(invoice_ids=bill_id)
    await crypto.close()

    if status.status == InvoiceStatus.PAID:
        await callback.answer("Платеж прошел успешно")
        await add_balance(session, float(amount), callback.from_user.id)
        await manager.done()

    else:
        await callback.answer("Платеж пока не получен")
