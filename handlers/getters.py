from aiogram_dialog import DialogManager
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.category import get_categories
from database.command.item import get_items, get_items_by_subcategory, get_item
from database.command.purchases import get_purchases
from database.command.subcategory import get_subcategories
from database.command.user import get_user
from dictionary.dictionary_ru import LEXICON_ASSORTIMENT


async def get_category(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    db_categories = await get_categories(session)
    data = {
        "categories": [
            (categories, categories.id)
            for categories in db_categories
        ]
    }
    return data


async def get_subcategory(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get("category_id")
    if not category_id:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("error_categories"))
        await dialog_manager.back()
        return

    db_subcategories = await get_subcategories(session, int(category_id))

    if len(db_subcategories) == 0:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("not_subcategories"))
        await dialog_manager.back()
        return

    data = {
        "subcategories": [
            (subcategories, subcategories.id)
            for subcategories in db_subcategories
        ]
    }
    return data


async def get_product(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    ctx = dialog_manager.current_context()
    subcategory_id = ctx.dialog_data.get("subcategory_id")

    if not subcategory_id:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("error_subcategories"))
        await dialog_manager.back()
        return

    db_product = await get_items_by_subcategory(session, int(subcategory_id))

    if len(db_product) == 0:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("not_items"))
        await dialog_manager.back()
        return

    data = {
        "product": [
            (product, product.id)
            for product in db_product  # TODO: Добавить количество товара и отправлять дату не строкой
        ]
    }
    return data


async def get_product_info(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    ctx = dialog_manager.current_context()
    product_id = ctx.dialog_data.get("product_id")
    if not product_id:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("error_items"))
        await dialog_manager.back()
        return

    db_product_info = await get_item(session, int(product_id))
    data = {
        "product": db_product_info
    }
    return data


async def get_buy_product(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    ctx = dialog_manager.current_context()
    product_id = ctx.start_data.get("product_id")
    if not product_id:
        await dialog_manager.event.answer(LEXICON_ASSORTIMENT.get("error_items"))
        await dialog_manager.back()
        return

    db_product_info = await get_item(session, int(product_id))

    amount = ctx.dialog_data.get("amount")

    data = {
        "product": db_product_info,
        "amount_user": amount,
        "total_amount": db_product_info.price * amount if amount else None
    }
    return data


async def get_confirm_add(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    data = ctx.dialog_data

    data_ret = {
        "category": int(data.get("subcategory_id")),
        "subcategory": int(data.get("subcategory_id")),
        "name": data.get("name"),
        "amount": len(data.get("files", [])),
        "photo": data.get("photo"),
        "price": data.get("price"),
        "description": data.get("description"),
    }

    return data_ret


async def get_profile(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    id_user = dialog_manager.event.from_user.id
    user = await get_user(session, id_user)
    data = {
        "user_id": user.id,
        "full_name": dialog_manager.event.from_user.full_name,
        "username": dialog_manager.event.from_user.username,
        "balance": user.balance,
        "register_time": user.register_time
    }
    return data


async def get_orders(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    id_user = dialog_manager.event.from_user.id
    user = await get_user(session, id_user)
    purchases = await get_purchases(session, user.id)
    data = {"orders": [
        (await get_item(session, pur.item_id), pur.amount, pur.id)
        for pur in purchases
    ]
    }
    return data


async def item_files_getter(dialog_manager: DialogManager, **kwargs) -> dict:
    """Data getter for set_item_photos window"""

    selected_files = dialog_manager.dialog_data.get("files", [])

    return {"files_count": len(selected_files)}