async def on_chosen_subcategories(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)
    menu = ctx.dialog_data.get("menu")

    if menu == "add_item":
        await manager.switch_to(AddItem.name)

    if menu == "del_item":
        await manager.switch_to(AddItem.select_item)

    if menu == "add_files":
        await manager.switch_to(AddItem.select_item)


async def on_chosen_items(callback: CallbackQuery, widget: Select, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(item_id=item_id)

    menu = ctx.dialog_data.get("menu")

    if menu == "del_item":
        await manager.switch_to(AddItem.del_item)

    if menu == "add_files":
        await manager.switch_to(AddItem.add_files)


async def on_chosen_amount(message: Message, input_message: MessageInput, manager: DialogManager):
    ctx = manager.current_context()

    files: list = ctx.dialog_data.get("files")

    if not files:
        ctx.dialog_data["files"] = []

    ctx.dialog_data.get("files").extend([message.document.file_id])
    ctx.dialog_data.update(quantity=len(ctx.dialog_data["files"]))


async def on_confirm_add_item(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    data = ctx.dialog_data
    item = ItemModel(**data)
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


async def on_del_item(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    item_id = int(ctx.dialog_data.get("item_id"))

    await delete_item(session, item_id)
    await callback.answer(LEXICON_ITEM.get("successful_del_item"))

    await manager.done()
