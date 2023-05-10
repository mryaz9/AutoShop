from aiogram_dialog import DialogManager
from loguru import logger

from database.command import item, category
from database.command.item import count_items
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
        await dialog_manager.event.answer("Нет товаров")
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
    logger.info(int(subcategory_id))
    db_product = await item.get_items(subcategory_id=int(subcategory_id))
    data = {
        "product": [
            (product, product.id)
            for product in db_product  # TODO: Добавить количество товара и отправлять дату не строкой
        ]
    }
    logger.info(data)
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
        "name":  data.get("name"),
        "amount": data.get("amount"),
        "photo": data.get("photo"),
        "price": data.get("price"),
        "time_action": data.get("time_action"),
        "description": data.get("description"),
    }

    return data_ret
