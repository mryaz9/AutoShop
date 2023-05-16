from dataclasses import dataclass
from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.category import create_category
from database.command.item import create_item, hide_item
from database.command.subcategory import create_subcategory
from database.command.user import create_admin
from database.models import Category, SubCategory, Items
from handlers.admin.states import AddItem, AddCategories
from dictionary.dictionary_ru import LEXICON_ITEM, LEXICON_CATEGORIES, LEXICON_ADMIN, LEXICON_MAILING
from schemas.admin import ItemModel, CategoryModel, SubCategoryModel
from utils.mailing_user import mailing

# TODO: Добавить дата класс в контексный менеджер
@dataclass()
class DialogData:
    category_id = None
    subcategory_id = None
    name = None
    amount = None
    photo = None
    price = None
    time_action = None
    description = None
    admin_id_add = None


async def on_chosen_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await manager.switch_to(AddItem.select_subcategories)


async def on_chosen_subcategories(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)
    menu = ctx.dialog_data.get("menu")

    if menu == "add_item":
        await manager.switch_to(AddItem.name)

    elif menu == "hide_item":
        await manager.switch_to(AddItem.hide_item)


async def on_chosen_name(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(name=message.text)
    await manager.switch_to(AddItem.amount)


async def on_chosen_amount(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(amount=int(message.text))
        await manager.switch_to(AddItem.photo)


async def on_chosen_photo(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(photo=message.photo[-1].file_id)
    await manager.switch_to(AddItem.price)


async def on_chosen_price(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(price=int(message.text))
        await manager.switch_to(AddItem.time_action)


async def on_chosen_time_action(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(time_action=int(message.text))
        await manager.switch_to(AddItem.description)


async def on_chosen_description(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(description=message.text)
    await manager.switch_to(AddItem.confirm)


async def on_chosen_confirm(callback: CallbackQuery, widget: Any, manager: DialogManager, session: AsyncSession):
    ctx = manager.current_context()
    data = ctx.dialog_data
    print(data)

    item = ItemModel()

    await create_item(session, item)

    await manager.event.answer(LEXICON_ITEM.get("done"))
    await manager.done()


async def on_select_add_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await manager.switch_to(AddCategories.add_subcategories)


async def on_add_category(message: Message, input_message: MessageInput, manager: DialogManager, session: AsyncSession):
    category = CategoryModel()
    category.title = message.text
    category.photo = "none"
    await create_category(session, category)

    await manager.event.answer(LEXICON_CATEGORIES.get("successful_add_category").format(category))
    await manager.done()


async def on_add_subcategory(message: Message, input_message: MessageInput,
                             manager: DialogManager, session: AsyncSession):

    ctx = manager.current_context()

    subcategory = SubCategoryModel()
    subcategory.title = message.text
    subcategory.category_id = ctx.dialog_data.get("category_id")
    subcategory.photo = "none"

    await create_subcategory(session, subcategory)

    await manager.event.answer(LEXICON_CATEGORIES.get("successful_add_subcategory").format(subcategory))
    await manager.done()


async def on_add_admin(message: Message, input_message: MessageInput, manager: DialogManager, session: AsyncSession):
    if message.text.isdigit():
        admin_id = int(message.text)
        admin = await create_admin(session, admin_id)
        if admin:
            await manager.event.answer(LEXICON_ADMIN.get("successful_add_admin").format(admin_id))
        elif not admin:
            await manager.event.answer(LEXICON_ADMIN.get("successful_del_admin").format(admin_id))
        await manager.done()


async def on_create_mailing(message: Message, input_message: MessageInput, manager: DialogManager, session: AsyncSession):
    mailing_text = message.text
    await manager.event.answer(LEXICON_MAILING.get("successful_add_mailing"))
    await mailing(session, mailing_text)
    await manager.done()


async def on_hide_item(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str, session: AsyncSession):
    show = await hide_item(session, int(item_id))
    if show:
        await manager.event.answer(LEXICON_ITEM.get("hide_on"), show_alert=True)

    elif not show:
        await manager.event.answer(LEXICON_ITEM.get("hide_off"), show_alert=True)


async def on_select_menu(callback: CallbackQuery, widget: Any, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(menu=widget.widget_id)
