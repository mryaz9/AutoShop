from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button

from database.command.category import create_category, delete_category, update_category
from database.command.item import create_item, delete_item, add_files, update_item
from database.command.main_menu import create_menu
from database.command.subcategory import create_subcategory, delete_subcategory, update_subcategory
from database.command.user import create_admin
from dictionary.dictionary_ru import LEXICON_ITEM, LEXICON_CATEGORIES, LEXICON_ADMIN, LEXICON_MAILING
from handlers.admin.states import AddItem, AddCategories
from schemas.admin import ItemModel, CategoryModel, SubCategoryModel, MenuModel
from utils.mailing_user import mailing_user


async def on_chosen_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=int(item_id))
    await manager.switch_to(AddItem.select_subcategories)


async def on_chosen_subcategories(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)
    menu = ctx.dialog_data.get("menu")

    if menu == "add_item":
        await manager.switch_to(AddItem.name)

    await manager.switch_to(AddItem.select_item)


async def on_chosen_items(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(item_id=item_id)

    menu = ctx.dialog_data.get("menu")

    if menu == "del_item":
        await manager.switch_to(AddItem.del_item)

    if menu == "add_files":
        await manager.switch_to(AddItem.add_files)

    await manager.switch_to(AddItem.name)


async def on_chosen_name(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(title=message.text)
    await manager.switch_to(AddItem.amount)


async def on_chosen_amount(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()

    files: list = ctx.dialog_data.get("files")

    if not files:
        ctx.dialog_data["files"] = []

    ctx.dialog_data.get("files").extend([message.document.file_id])
    ctx.dialog_data.update(quantity=len(ctx.dialog_data["files"]))


async def on_chosen_photo(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(photo=message.photo[-1].file_id)
    await manager.switch_to(AddItem.price)


async def on_chosen_price(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(price=float(message.text))
        await manager.switch_to(AddItem.description)


async def on_chosen_description(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(description=message.text)
    await manager.switch_to(AddItem.confirm)


async def on_chosen_confirm(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    data = ctx.dialog_data
    item = ItemModel(**data)

    if data.get("menu") == "change_item":
        item_id = int(data.get("item_id"))
        await update_item(session, item_id, item)

    else:
        await create_item(session, item)

    await callback.answer(LEXICON_ITEM.get("done"))
    await manager.done()


async def on_add_files_confirm(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    data = ctx.dialog_data
    item_id = data.get("item_id")
    files = data.get("files")

    await add_files(session, int(item_id), files)
    await manager.done()


async def on_select_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)

    if ctx.dialog_data.get("menu") == "add_subcategory":
        await manager.switch_to(AddCategories.input_name_subcategories)

    if ctx.dialog_data.get("menu") == "change_subcategory":
        await manager.switch_to(AddCategories.select_subcategories)

    if ctx.dialog_data.get("menu") == "change_category":
        await manager.switch_to(AddCategories.input_name_categories)

    if ctx.dialog_data.get("menu") == "del_categories":
        await manager.switch_to(AddCategories.del_categories)

    if ctx.dialog_data.get("menu") == "del_subcategories":
        await manager.switch_to(AddCategories.select_subcategories)


async def on_select_subcategory(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)

    if ctx.dialog_data.get("menu") == "del_categories":
        await manager.switch_to(AddCategories.del_subcategories)

    if ctx.dialog_data.get("menu") == "change_subcategory":
        await manager.switch_to(AddCategories.input_name_subcategories)


async def on_input_name_category(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(title=message.text)
    await manager.switch_to(AddCategories.input_photo_categories)


async def on_input_photo_category(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(photo=message.photo[-1].file_id)
    await manager.switch_to(AddCategories.add_categories)


async def on_add_categories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    data = ctx.dialog_data

    category = CategoryModel(**data)

    if ctx.dialog_data.get("menu") == "change_category":
        category_id = ctx.dialog_data.get("category_id")
        await update_category(session, int(category_id), category)

    if ctx.dialog_data.get("menu") == "add_category":
        await create_category(session, category)

    await callback.answer(LEXICON_CATEGORIES.get("successful_add_category"))
    await manager.done()


async def on_input_name_subcategory(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(title=message.text)
    await manager.switch_to(AddCategories.input_photo_subcategories)


async def on_input_photo_subcategory(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(photo=message.photo[-1].file_id)
    await manager.switch_to(AddCategories.add_subcategories)


async def on_add_subcategories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    data = ctx.dialog_data

    subcategory = SubCategoryModel(**data)

    if ctx.dialog_data.get("menu") == "change_subcategory":
        subcategory_id = ctx.dialog_data.get("subcategory_id")
        await update_subcategory(session, int(subcategory_id), subcategory)

    if ctx.dialog_data.get("menu") == "add_subcategory":
        await create_subcategory(session, subcategory)

    await callback.answer(
        LEXICON_CATEGORIES.get("successful_add_subcategory"))
    await manager.done()


async def on_add_admin(message: Message, input_message: MessageInput, manager: DialogManager):
    session = manager.middleware_data.get("session")
    if message.text.isdigit():
        admin_id = int(message.text)
        admin = await create_admin(session, admin_id)
        if admin:
            await manager.event.answer(LEXICON_ADMIN.get("successful_add_admin").format(admin_id=admin_id))
        elif not admin:
            await manager.event.answer(LEXICON_ADMIN.get("successful_del_admin").format(admin_id=admin_id))
        await manager.done()


async def on_del_admin(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    session = manager.middleware_data.get("session")

    admin_id = int(item_id)
    await create_admin(session, admin_id)
    await manager.event.answer(LEXICON_ADMIN.get("successful_del_admin").format(admin_id=admin_id))
    await manager.done()


async def on_create_mailing(message: Message, input_message: MessageInput, manager: DialogManager):
    session = manager.middleware_data.get("session")
    mailing_text = message.text
    await manager.event.answer(LEXICON_MAILING.get("successful_add_mailing"))
    await mailing_user(session, mailing_text)
    await manager.done()


async def on_del_categories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    category_id = int(ctx.dialog_data.get("category_id"))

    await delete_category(session, category_id)
    await callback.answer(LEXICON_CATEGORIES.get("successful_del_categories"))

    await manager.done()


async def on_del_subcategories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    subcategory_id = int(ctx.dialog_data.get("subcategory_id"))

    await delete_subcategory(session, subcategory_id)
    await callback.answer(LEXICON_CATEGORIES.get("successful_del_subcategories"))

    await manager.done()


async def on_del_item(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    item_id = int(ctx.dialog_data.get("item_id"))

    await delete_item(session, item_id)
    await callback.answer(LEXICON_ITEM.get("successful_del_item"))

    await manager.done()


async def on_select_menu(callback: CallbackQuery, widget: Any, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(menu=widget.widget_id)


async def confirm_change_menu(callback: CallbackQuery, btn: Button, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()

    menu = MenuModel(**ctx.widget_data)
    await create_menu(session, menu)

    await manager.done()

# TODO: Обернуть все запросы в бд
# except DBAPIError:
#    await callback.answer(LEXICON_CATEGORIES.get("error_db"))
