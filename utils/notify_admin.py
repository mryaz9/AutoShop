import asyncio

from aiogram import Bot, types
from loguru import logger

from config.config import Config, load_config
from database.command.user import get_all_admin
from dictionary.dictionary_ru import LEXICON_ADMIN_INFO


async def startup(bot):
    logger.info("Бот запущен")


async def shutdown(bot):
    logger.info("Бот остановлен")


async def new_order(sessionmaker, message_text):
    config: Config = load_config()

    bot = Bot(token=config.bot.token)

    for admin in await get_all_admin(sessionmaker):
        try:
            await bot.send_message(chat_id=int(admin.user_id), text=message_text)
            await asyncio.sleep(1)
        except:
            logger.info(f"Не получилось отправить сообщение {admin}")

    await bot.close()
