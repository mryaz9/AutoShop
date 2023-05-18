import asyncio

from aiogram import Bot, types
from aiogram.client.session.base import BaseSession
from aiogram.exceptions import TelegramBadRequest
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

    bot: Bot = Bot(token=config.bot.token)

    for admin in await get_all_admin(sessionmaker):
        try:
            await bot.send_message(chat_id=int(admin.id), text=message_text, disable_notification=notify)
            await asyncio.sleep(1)
            break
        except TelegramBadRequest:
            logger.info(f"Не получилось отправить сообщение {admin.id}")
            await bot.send_message(chat_id=int(admin.id), text=message_text, disable_notification=notify)
            await asyncio.sleep(30)

