from typing import Any

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, DialogProtocol
from aiogram_dialog.widgets.input import MessageInput

from database.command.category import get_categories, get_subcategories
from database.command.item import add_item
from dialogs.admin.states import AddItem, Category, SubCategory, Product
from lexicon.lexicon_ru import LEXICON_FSM_SHOP


async def on_chosen_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):

    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)
    await manager.start(SubCategory.select_subcategories, data=ctx)


async def on_chosen_subcategories(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    category_id = ctx.start_data.get("category_id")
    ctx.dialog_data.update(category_id=category_id)
    ctx.dialog_data.update(subcategory_id=item_id)
    await manager.start(Product.select_product, data=ctx)


async def on_chosen_products(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    category_id = ctx.start_data.get("category_id")
    subcategory_id = ctx.start_data.get("subcategory_id")
    ctx.dialog_data.update(category_id=category_id)
    ctx.dialog_data.update(subcategory_id=subcategory_id)
    ctx.dialog_data.update(product=item_id)

    await manager.start(Product.select_product, data=ctx)


async def on_chosen_name(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(name=message.text)
    await manager.switch_to(AddItem.amount)


async def on_chosen_amount(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(amount=message.text)
        await manager.switch_to(AddItem.files)


async def on_chosen_files(message: Message, input_message: MessageInput, manager: DialogManager):
    print(message)
    if message.text.isdigit() and message.text == "0":
        ctx = manager.current_context()
        ctx.dialog_data.update(files=None)
        await manager.switch_to(AddItem.photo)

    else:
        ctx = manager.current_context()
        ctx.dialog_data.update(files=message.document.file_id)
        print(message.document.file_id)
        await manager.switch_to(AddItem.photo)


async def on_chosen_photo(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(photo=message.photo[-1].file_id)
    await manager.switch_to(AddItem.price)


async def on_chosen_price(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(price=message.text)
        await manager.switch_to(AddItem.time_action)


async def on_chosen_time_action(message: Message, input_message: MessageInput, manager: DialogManager):
    if message.text.isdigit():
        ctx = manager.current_context()
        ctx.dialog_data.update(time_action=message.text)
        await manager.switch_to(AddItem.description)


async def on_chosen_description(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(description=message.text)
    await manager.switch_to(AddItem.confirm)


async def on_chosen_confirm(callback: CallbackQuery, widget: Any, manager: DialogManager):
    ctx = manager.current_context()
    data = ctx.dialog_data
    admin_id_add = callback.from_user.id

    await add_item(show=True, category_code=data["category_id"],
                   category_name=data["category_name"], subcategory_name=data["subcategory_name"],
                   subcategory_code=data["subcategory_id"], name=data["name"],
                   amount=int(data["amount"]), photo=data["photo"],
                   price=int(data["price"]), time_action=int(data["time_action"]),
                   description=data["description"], admin_id_add=admin_id_add)

    await manager.event.answer(LEXICON_FSM_SHOP["done_yes"])
    await manager.done()



async def on_add_new_category_name(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_name=message.text)
    await manager.switch_to(Category.add_new_subcategories_code)


async def on_add_new_subcategory_code(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=message.text)
    await manager.switch_to(AddItem.add_new_subcategories_name)


async def on_add_new_subcategory_name(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_name=message.text)
    await manager.switch_to(AddItem.name)


