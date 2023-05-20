async def on_create_mailing(message: Message, input_message: MessageInput, manager: DialogManager):
    session = manager.middleware_data.get("session")
    mailing_text = message.text
    await manager.event.answer(LEXICON_MAILING.get("successful_add_mailing"))
    await mailing_user(session, mailing_text)
    await manager.done()