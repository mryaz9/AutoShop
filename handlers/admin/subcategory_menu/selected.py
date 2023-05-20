async def on_select_category(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(category_id=item_id)

    if ctx.dialog_data.get("menu") == "add_subcategory":
        await manager.switch_to(AddCategories.input_name_subcategories)

    elif ctx.dialog_data.get("menu") == "del_categories":
        await manager.switch_to(AddCategories.del_categories)

    elif ctx.dialog_data.get("menu") == "del_subcategories":
        await manager.switch_to(AddCategories.select_subcategories)


async def on_select_subcategory(callback: CallbackQuery, widget: Any, manager: DialogManager, item_id: str):
    ctx = manager.current_context()
    ctx.dialog_data.update(subcategory_id=item_id)
    await manager.switch_to(AddCategories.del_subcategories)


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

    await create_subcategory(session, subcategory)

    await callback.answer(
        LEXICON_CATEGORIES.get("successful_add_subcategory"))
    await manager.done()


async def on_del_subcategories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    subcategory_id = int(ctx.dialog_data.get("subcategory_id"))

    await delete_subcategory(session, subcategory_id)
    await callback.answer(LEXICON_CATEGORIES.get("successful_del_subcategories"))

    await manager.done()
