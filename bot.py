import asyncio
import logging

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from aiogram import Bot, Dispatcher
from aiogram_dialog.tools import render_transitions, render_preview
from loguru import logger

from dialogs.admin import admin_dialogs
from dialogs.assortiment import items_dialogs
from dialogs.main_menu import main_menu_dialogs
from dialogs.profile import profile_dialogs
from handlers import user, other
from config.config import Config, load_config

from database.init_database import create_db
from database.command.admin import add_new_admin
from payment import payment_dialogs


def register_all_dialog(dp):
    dialogs = [
        items_dialogs,
        admin_dialogs,
        main_menu_dialogs,
        profile_dialogs,
        payment_dialogs
    ]

    for dialog in dialogs:
        for i in dialog():
            # logger.info(i.windows)
            # render_transitions(i, title=i.__name__)
            dp.include_router(i)

    setup_dialogs(dp)


def register_all_handlers(dp):
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)
    dp.include_router(user.router)
    dp.include_router(other.router)


async def creating_db(config):
    await create_db()
    for admin in config.tg_bot.admin_ids:
        await add_new_admin(int(admin))


# Функция конфигурирования и запуска бота
async def main():
    # Выводим в консоль информацию о начале запуска бота
    config: Config = load_config()
    """storage = RedisStorage(
        Redis(host=config.tg_bot.ip),
        # in case of redis you need to configure key builder
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )"""
    storage = MemoryStorage()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    await creating_db(config)
    register_all_dialog(dp)
    register_all_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

    # Проверяет старые апдейты с учетом имеющихся хендлеров
    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

