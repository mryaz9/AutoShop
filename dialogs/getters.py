from aiogram_dialog import DialogManager
from loguru import logger

from database.command import item, category
from database.command.item import count_items, get_item
from database.command.purchases import get_purchases
from database.command.user import get_user
from dialogs.assortiment.states import BotMenu


async def get_categories(dialog_manager: DialogManager, **kwargs):
    db_categories = await category.get_categories()
    data = {
        "categories": [
            (categories.category_name, categories.id)
            for categories in db_categories
        ]
    }
    return data


async def get_subcategories(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get("category_id")
    if not category_id:
        await dialog_manager.event.answer("Сначала выберете категорию")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    db_subcategories = await category.get_subcategories(category_id=int(category_id))
    if len(db_subcategories) == 0:
        await dialog_manager.event.answer("Нет подкатегорий")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    data = {
        "subcategories": [(subcategories.subcategory_name, subcategories.id)
                          for subcategories in db_subcategories
                          ]
    }
    return data


async def get_product(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    subcategory_id = ctx.dialog_data.get("subcategory_id")

    if not subcategory_id:
        await dialog_manager.event.answer("Сначала выберете подкатегорию")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    db_product = await item.get_items(subcategory_id=int(subcategory_id))

    if len(db_product) == 0:
        await dialog_manager.event.answer("Нет товаров")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    data = {
        "product": [
            (product, product.id)
            for product in db_product  # TODO: Добавить количество товара и отправлять дату не строкой
        ]
    }
    return data


async def get_product_info(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    product_id = ctx.dialog_data.get("product_id")
    if not product_id:
        await dialog_manager.event.answer("Сначала выберете продукт")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    db_product_info = await item.get_item(int(product_id))

    data = {
        "product": db_product_info
    }
    return data


async def get_buy_product(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    product_id = ctx.start_data.get("product_id")
    if not product_id:
        await dialog_manager.event.answer("Сначала выберете продукт")
        await dialog_manager.switch_to(BotMenu.select_categories)
        return

    db_product_info = await item.get_item(int(product_id))
    amount = ctx.dialog_data.get("amount")

    data = {
        "product": db_product_info.name,
        "amount": db_product_info.amount,
        "amount_user": amount,
        "total_amount": db_product_info.price * amount if amount else None
    }
    return data


async def get_confirm_add(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    data = ctx.dialog_data

    data_ret = {
        "subcategory_id": int(data.get("subcategory_id")),
        "name": data.get("name"),
        "amount": data.get("amount"),
        "photo": data.get("photo"),
        "price": data.get("price"),
        "time_action": data.get("time_action"),
        "description": data.get("description"),
    }

    return data_ret


async def get_profile(dialog_manager: DialogManager, **kwargs):
    id_user = dialog_manager.event.from_user.id
    user = await get_user(id_user)
    data = {
        "user_id": user.user_id,
        "full_name": user.full_name,
        "username": user.username,
        "balance": user.balance,
        "register_time": user.register_time
    }
    return data


async def get_order(dialog_manager: DialogManager, **kwargs):
    id_user = dialog_manager.event.from_user.id
    user = await get_user(id_user)
    purchases = await get_purchases(user.id)
    data = {"orders": [
        (await get_item(pur.item_id), pur.amount, pur.id)
        for pur in purchases
    ]
    }

    return data
