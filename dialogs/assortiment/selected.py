from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput

from database.command.database_item import get_item
from dialogs.assortiment.states import BotMenu, BuyProduct


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
    await manager.start(BuyProduct.enter_amount, data={
        "product_id": product_id
    })


async def on_entered_amount(message: Message, widget: TextInput, manager: DialogManager, amount: str):
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")
    if not amount.isdigit():
        await message.answer("Введите число")
        return
    amount = int(amount)
    product_info = await get_item(int(product_id))
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
    product_info = await get_item(int(product_id))
    await callback.answer(f"Вы купили {amount} {product_info.name}")
    await manager.done(result={
        "switch_to_window": "select_products"
    })