from aiogram_dialog import DialogManager

from database.command import database_item
from database.command.database_item import count_items
from dialogs.admin.states import AdminMenu


async def get_categories(dialog_manager: DialogManager, **kwargs):
    db_categories = await database_item.get_categories()
    data = {
        "categories": [
            (f'{category.category_name} ({await count_items(category.category_code)})', category.category_code)
            for category in db_categories
        ]
    }
    return data


async def get_subcategories(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get("category_id")
    if not category_id:
        await dialog_manager.event.answer("Сначала выберете категорию")
        await dialog_manager.switch_to(AdminMenu.select_categories)
        return

    db_subcategories = await database_item.get_subcategories(category=category_id)

    data = {
        "subcategories": [
            (f'{subcategories.subcategory_name} ({await count_items(category_id, subcategories.subcategory_code)})',
             subcategories.subcategory_code)
            for subcategories in db_subcategories
        ]
    }
    return data


async def get_product(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get("category_id")
    subcategory_id = ctx.dialog_data.get("subcategory_id")

    if not category_id or not subcategory_id:
        await dialog_manager.event.answer("Сначала выберете подкатегорию")
        await dialog_manager.switch_to(AdminMenu.select_categories)
        return

    db_product = await database_item.get_items(category_code=category_id, subcategory_code=subcategory_id)
    data = {
        "product": [
            (f'{product.name} {product.amount} {product.price}', product.id)  # TODO: Добавить количество товара
            for product in db_product
        ]
    }
    return data
