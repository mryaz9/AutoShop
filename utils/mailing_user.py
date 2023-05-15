import asyncio

from aiogram import types, Bot
from loguru import logger

from config.config import Config, load_config
from database.command.user import get_all_user


async def mailing(mailing_text):
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    for users in await get_all_user():
        try:
            await bot.send_message(
                chat_id=users.user_id,
                text=mailing_text)
            await asyncio.sleep(1)
        except:
            logger.info(f"Не получилось отправить сообщение {users}")

    await bot.close()
