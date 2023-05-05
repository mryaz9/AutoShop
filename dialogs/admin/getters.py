from aiogram_dialog import DialogManager

from database.command import database_item
from database.command.database_item import count_items
from dialogs.admin.states import AdminMenu, AddAssortiment


async def get_categories(dialog_manager: DialogManager, **kwargs):
    db_categories = await database_item.get_categories()
    data = {
        "categories": [
            (f'{category.category_name} ({await count_items(category.category_code)})',
             category.category_code)
            for category in db_categories
        ]
    }
    return data


async def get_subcategories(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    category_id = ctx.dialog_data.get("category_id")
    if not category_id:
        await dialog_manager.event.answer("Сначала выберете категорию")
        await dialog_manager.switch_to(AddAssortiment.select_categories)
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


async def get_confirm_add(dialog_manager: DialogManager, **kwargs):
    ctx = dialog_manager.current_context()
    return ctx.dialog_data
