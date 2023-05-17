import datetime
from typing import Any, Sequence

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.item import get_item, get_files
from database.command.purchases import add_order, get_purchases
from database.command.user import get_user, reduce_balance
from database.models import Order
from handlers.users.assortiment.states import BotMenu, BuyProduct
from dictionary.dictionary_ru import LEXICON_ASSORTIMENT
from utils.notify_admin import new_order


async def on_chosen_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await manager.switch_to(BotMenu.select_subcategories)


async def on_chosen_subcategories(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)
    await manager.switch_to(BotMenu.select_product)


async def on_chosen_product(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(product_id=item_id)
    await manager.switch_to(BotMenu.select_product_info)


async def on_chosen_product_info(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    product_id = ctx.dialog_data.get("product_id")
    # Todo: Добавить проверку на тип товара
    # Todo: Проверка на наличие файлов, если нет, то сразу перекидывает в покупку
    files = await get_files(session, int(product_id))

    if len(files) == 0:
        await manager.start(BuyProduct.confirm, data={
            "product_id": product_id})
    else:
        await manager.start(BuyProduct.enter_amount, data={
            "product_id": product_id})


async def on_entered_amount(message: Message, widget: TextInput, manager: DialogManager, amount: str):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")

    if not amount.isdigit():
        await message.answer(LEXICON_ASSORTIMENT.get("error_input_amount"))
        return

    amount = int(amount)
    product_info = await get_files(session, int(product_id))

    if product_info is not None:
        if len(product_info) < amount:
            await message.answer(LEXICON_ASSORTIMENT.get("error_not_items"))
            return

    ctx.dialog_data.update(amount=amount)
    await manager.switch_to(BuyProduct.confirm)


async def on_confirm_buy(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")

    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")
    amount = ctx.dialog_data.get("amount")
    # TODO: Запрос в бд для покупки товара
    user = await get_user(session, int(callback.from_user.id))

    product_info = await get_item(session, int(product_id))

    if callback.from_user.username is None:
        await callback.answer(LEXICON_ASSORTIMENT.get("error_unknown_username"), show_alert=True)
        return

    # TODO: Выбор способа оплаты
    if user.balance < product_info.price:
        await callback.answer(LEXICON_ASSORTIMENT.get("error_not_money"), show_alert=True)
        return

    purchases = Order(buyer_id=user.id,
                          item_id=int(product_id),
                          amount=int(amount),
                          purchase_time=datetime.datetime.now())

    await add_order(session, purchases)

    await reduce_balance(session, product_info.price, user.id)

    await callback.answer(LEXICON_ASSORTIMENT.get("successful_buy_item").format(amount=amount, name=product_info.name),
                          show_alert=True)

    purchases_get: Sequence[Order] = await get_purchases(session, user.id)
    purchases_get: Order = purchases_get[-1]

    username = callback.from_user.username
    full_name = callback.from_user.full_name

    message_text = LEXICON_ASSORTIMENT.get("send_admin_buy").format(
        id=purchases_get.id, name=product_info.name,
        amount=purchases_get.amount, full_name=full_name, username=username)

    await new_order(session, message_text)

    await manager.done(result={
        "switch_to_window": "select_products"
    })
