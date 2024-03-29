import asyncio
import logging

from aiogram import Bot, exceptions

from config.config import Config, load_config
from database.command.user import get_all_user


async def mailing_user(sessionmaker, mailing_text):
    config: Config = load_config()

    bot = Bot(token=config.bot.token)

    for admin in await get_all_user(sessionmaker):
        try:
            await bot.send_message(chat_id=int(admin.id), text=mailing_text)
            await asyncio.sleep(1)
        except exceptions.TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            await bot.send_message(chat_id=int(admin.id), text=mailing_text)
        except exceptions.TelegramBadRequest as e:
            logging.info(f"Не получилось отправить сообщение {admin.id}\n{e}")

    await bot.session.close()
