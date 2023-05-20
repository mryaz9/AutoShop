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