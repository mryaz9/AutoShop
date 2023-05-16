import asyncio

from aiogram import types, Bot
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession

from config.config import Config, load_config
from database.command.user import get_all_user


async def mailing(session: AsyncSession, mailing_text: str):
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    for users in await get_all_user(session):
        try:
            await bot.send_message(
                chat_id=users.id,
                text=mailing_text)
            await asyncio.sleep(1)
        except:
            logger.info(f"Не получилось отправить сообщение {users.id}")

    await bot.close()
