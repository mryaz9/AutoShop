import asyncio
from operator import attrgetter

from aiogram import Bot, types, exceptions
from aiogram.client.session.base import BaseSession
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram_broadcaster import TextBroadcaster
from loguru import logger

from config.config import Config, load_config
from database.command.user import get_all_admin
from dictionary.dictionary_ru import LEXICON_ADMIN_INFO


async def startup(bot):
    logger.info("Бот запущен")


async def shutdown(bot):
    logger.info("Бот остановлен")


async def new_order(sessionmaker, message_text, notify=True):
    config: Config = load_config()

    bot = Bot(token=config.bot.token)

    for admin in await get_all_admin(sessionmaker):
        try:
            await bot.send_message(chat_id=int(admin.id), text=message_text)
            await asyncio.sleep(1)
        except exceptions.TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            await bot.send_message(chat_id=int(admin.id), text=message_text)
        except exceptions.TelegramBadRequest as e:
            logger.info(f"Не получилось отправить сообщение {admin}\n{e}")

    await bot.session.close()
