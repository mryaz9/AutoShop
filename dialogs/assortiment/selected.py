import datetime
from typing import Any

from aiogram.methods import export_chat_invite_link
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from loguru import logger

from database.command.item import get_item
from database.command.purchases import add_purchases, get_purchases
from database.command.user import get_user, reduce_balance
from database.models import Purchases
from dialogs.assortiment.states import BotMenu, BuyProduct
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


async def on_entered_amount(message: Message, widget: TextInput, manager: DialogManager, amount: str):
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")
    if not amount.isdigit():
        await message.answer("Введите число")
        return
    amount = int(amount)
    product_info = await get_item(int(product_id))
    if product_info.amount is not None:
        if product_info.amount < amount:
            await message.answer("Недостаточно товаров")
            return
    ctx.dialog_data.update(amount=amount)
    await manager.switch_to(BuyProduct.confirm)


async def on_confirm_buy(callback: CallbackQuery, widget: Any, manager: DialogManager):
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")
    amount = ctx.dialog_data.get("amount")
    # TODO: Запрос в бд для покупки товара
    user = await get_user(int(callback.from_user.id))

    product_info = await get_item(int(product_id))

    if user.username is None:
        await callback.answer("Создайте user_name", show_alert=True)
        return

    # TODO: Выбор способа оплаты
    if user.balance < product_info.price:
        await callback.answer("Недостаточно средств", show_alert=True)
        return

    purchases = Purchases(buyer_id=user.id,
                          item_id=int(product_id),
                          amount=int(amount),
                          purchase_time=datetime.datetime.now())

    await add_purchases(purchases)

    await reduce_balance(product_info.price, user.user_id)

    await callback.answer(f"Вы купили {amount} {product_info.name}", show_alert=True)

    purchases_get: list[Purchases] = await get_purchases(user.id)
    purchases_get: Purchases = purchases_get[-1]
    user_name = user.username

    message_text = f"Номер заказа: #{purchases_get.id}\n" \
                   f"Товар: {product_info.name}\n" \
                   f"Кол-во: {purchases_get.amount}\n" \
                   f"Имя: {user.full_name}\n" \
                   f"Покупатель: @{user_name}\n" \

    await new_order(message_text)

    await manager.done(result={
        "switch_to_window": "select_products"
    })
