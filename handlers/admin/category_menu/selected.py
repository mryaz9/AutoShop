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

    await create_category(session, category)

    await callback.answer(LEXICON_CATEGORIES.get("successful_add_category"))
    await manager.done()


async def on_del_categories(callback: CallbackQuery, widget: Any, manager: DialogManager):
    session = manager.middleware_data.get("session")
    ctx = manager.current_context()
    category_id = int(ctx.dialog_data.get("category_id"))

    await delete_category(session, category_id)
    await callback.answer(LEXICON_CATEGORIES.get("successful_del_categories"))

    await manager.done()
