from typing import Any

from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, Message, InputMediaDocument
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button

from database.command.item import get_item, get_files, return_and_del_files
from database.command.user import get_user, reduce_balance
from dictionary.dictionary_ru import LEXICON_ASSORTIMENT
from handlers.users.assortiment.states import BotMenu, BuyProduct
from utils.notify_admin import new_order
from utils.other import parting


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
    # Todo: Проверка на наличие файлов, если нет, то сразу перекидывает в покупку

    await manager.start(BuyProduct.enter_amount,
                        data={
                            "product_id": product_id
                              }
                        )


async def on_entered_amount_counter(message: CallbackQuery, widget: Button, manager: DialogManager, ):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")

    amount_user = manager.find("counter_amount").get_value()

    product_info = await get_files(session, int(product_id))

    if product_info is not None:
        if (len(product_info) < amount_user) and (amount_user > 0):
            await message.answer(LEXICON_ASSORTIMENT.get("error_not_items"))
            return

        ctx.dialog_data.update(amount_user=amount_user)

    await manager.switch_to(BuyProduct.confirm)


async def on_entered_amount(message: Message, widget: TextInput, manager: DialogManager, item_id: str):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    product_id = ctx.start_data.get("product_id")

    if not item_id.isdigit():
        await message.answer(LEXICON_ASSORTIMENT.get("error_input_amount"))
        return

    amount_user = int(item_id)

    product_info = await get_files(session, int(product_id))

    if product_info is not None:
        if (len(product_info) < amount_user) and (amount_user > 0):
            await message.answer(LEXICON_ASSORTIMENT.get("error_not_items"))
            return

        ctx.dialog_data.update(amount_user=amount_user)

    await manager.switch_to(BuyProduct.confirm)


async def on_confirm_buy(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")

    ctx = manager.current_context()
    product_id = int(ctx.start_data.get("product_id"))

    if ctx.start_data.get("amount_user") is not None:
        amount_user = ctx.start_data.get("amount_user")
    else:
        amount_user = ctx.dialog_data.get("amount_user")

    user = await get_user(session, int(callback.from_user.id))

    product_info = await get_item(session, product_id)

    summ = product_info.price * amount_user

    # TODO: Выбор способа оплаты
    if user.balance < summ:
        await callback.answer(LEXICON_ASSORTIMENT.get("error_not_money"), show_alert=True)
        return

    files = await return_and_del_files(session, product_id, amount_user)

    list_files: list = []
    for i in files:
        list_files.append(InputMediaDocument(media=i))

    try:
        await callback.message.answer_media_group(media=list_files)
    except TelegramBadRequest:
        part = parting(list_files, 9)
        for i in part:
            await callback.message.answer_media_group(media=i)

    # TODO: Добавить файлы в заказ

    await reduce_balance(session, summ, user.id)

    await callback.answer(
        LEXICON_ASSORTIMENT.get("successful_buy_item").format(amount_user=amount_user, title=product_info.title),
        show_alert=True)

    await manager.done(result={
        "switch_to_window": "select_products"
    })
