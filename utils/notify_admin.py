import asyncio

from aiogram import Bot
from loguru import logger

from config.config import Config, load_config
from database.command.admin import get_all_admin
from lexicon.lexicon_ru import LEXICON_ADMIN_INFO


async def startup(bot):
    for admin in await get_all_admin():
        await bot.send_message(chat_id=int(admin.user_id), text=LEXICON_ADMIN_INFO["startup"])


async def shutdown(bot):
    for admin in await get_all_admin():
        await bot.send_message(chat_id=int(admin.user_id), text=LEXICON_ADMIN_INFO["shutdown"])


async def new_order(message_text):
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    for admin in await get_all_admin():
        try:
            await bot.send_message(chat_id=int(admin.user_id), text=message_text)
            await asyncio.sleep(1)
        except:
            logger.info(f"Не получилось отправить сообщение {admin}")