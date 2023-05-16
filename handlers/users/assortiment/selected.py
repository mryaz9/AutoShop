import datetime
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.item import get_item
from database.command.purchases import add_purchases, get_purchases
from database.command.user import get_user, reduce_balance
from database.models import Purchases
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
    ctx = manager.current_context()
    product_id = ctx.dialog_data.get("product_id")
    # Todo: Добавить проверку на тип товара
    # await manager.start(BuyProduct.enter_amount, data={
    #    "product_id": product_id})
    await manager.start(BuyProduct.enter_amount, data={
        "product_id": product_id})


async def on_entered_amount(message: Message, widget: TextInput, manager: DialogManager,
                            amount: str, session: AsyncSession):
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")

    if not amount.isdigit():
        await message.answer(LEXICON_ASSORTIMENT.get("error_input_amount"))
        return

    amount = int(amount)
    product_info = await get_item(session, int(product_id))

    if product_info.amount is not None:
        if product_info.amount < amount:
            await message.answer(LEXICON_ASSORTIMENT.get("error_not_items"))
            return

    ctx.dialog_data.update(amount=amount)
    await manager.switch_to(BuyProduct.confirm)


async def on_confirm_buy(callback: CallbackQuery, widget: Any,
                         manager: DialogManager, session: AsyncSession):
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")
    amount = ctx.dialog_data.get("amount")
    # TODO: Запрос в бд для покупки товара
    user = await get_user(session, int(callback.from_user.id))

    product_info = await get_item(session, int(product_id))

    if user.username is None:
        await callback.answer(LEXICON_ASSORTIMENT.get("error_unknown_username"), show_alert=True)
        return

    # TODO: Выбор способа оплаты
    if user.balance < product_info.price:
        await callback.answer(LEXICON_ASSORTIMENT.get("error_not_money"), show_alert=True)
        return

    purchases = Purchases(buyer_id=user.id,
                          item_id=int(product_id),
                          amount=int(amount),
                          purchase_time=datetime.datetime.now())

    await add_purchases(session, purchases)

    await reduce_balance(session, product_info.price, user.user_id)

    await callback.answer(LEXICON_ASSORTIMENT.get("error_not_money").format(amount, product_info.name), show_alert=True)

    purchases_get: list[Purchases] = await get_purchases(session, user.id)
    purchases_get: Purchases = purchases_get[-1]
    username = user.username

    message_text = LEXICON_ASSORTIMENT.get("send_admin_buy").format(
        purchases_get.id, product_info.name, purchases_get.amount, user.full_name, username)

    await new_order(session, message_text)

    await manager.done(result={
        "switch_to_window": "select_products"
    })
