import asyncio
import logging

from aiogram import Bot, exceptions
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot_tgc.config.config import Config, load_config
from bot_tgc.database.command.user import get_all_admin


async def startup(bot):
    logging.info("Бот запущен")


async def shutdown(bot):
    logging.info("Бот остановлен")


async def new_order(sessionmaker, message_text, user_id, notify=True):
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    kb = InlineKeyboardBuilder()
    kb.button(text="Написать покупателю", url=f"tg://user?id={user_id}")

    for admin in await get_all_admin(sessionmaker):
        try:
            await bot.send_message(chat_id=int(admin.id), text=message_text,
                                   reply_markup=kb.as_markup(), disable_notification=notify)
            await asyncio.sleep(1)
        except exceptions.TelegramRetryAfter as e:
            await asyncio.sleep(e.retry_after)
            await bot.send_message(chat_id=int(admin.id), text=message_text,
                                   reply_markup=kb.as_markup(), disable_notification=notify)
        except exceptions.TelegramBadRequest as e:
            logging.info(f"Не получилось отправить сообщение {admin}\n{e}")

    await bot.session.close()
