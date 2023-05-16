import asyncio
import logging

from aiogram.fsm.storage.memory import MemoryStorage, SimpleEventIsolation
from aiogram_dialog import setup_dialogs
from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker

from database import get_async_sessionmaker
from dialogs.admin import admin_dialogs
from dialogs.assortiment import items_dialogs
from dialogs.main_menu import main_menu_dialogs
from dialogs.profile import profile_dialogs
from handlers import user, other
from config.config import Config, load_config

from database.command.admin import add_new_admin
from middleware import DBSessionMiddleware, ConfigMiddleware
from payment import payment_dialogs
from utils.notify_admin import startup, shutdown


def register_dialog(dp):
    dialogs = [
        items_dialogs,
        admin_dialogs,
        main_menu_dialogs,
        profile_dialogs,
        payment_dialogs
    ]

    for dialog in dialogs:
        for i in dialog():
            dp.include_router(i)

    setup_dialogs(dp)


def register_handlers(dp):
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(user.router)
    dp.include_router(other.router)


def register_middleware(dp: Dispatcher, middleware) -> None:
    """Register middleware in 'message', 'callback' and 'update' layers of dp"""

    dp.message.outer_middleware(middleware)
    dp.callback_query.outer_middleware(middleware)
    dp.update.outer_middleware(middleware)


# Функция конфигурирования и запуска бота
async def main():
    # Выводим в консоль информацию о начале запуска бота
    config: Config = load_config()

    sessionmaker: async_sessionmaker = await get_async_sessionmaker(config)
    db_middleware = DBSessionMiddleware(sessionmaker)
    config_middleware = ConfigMiddleware(config)
    """storage = RedisStorage(
        Redis(host=config.tg_bot.ip),
        # in case of redis you need to configure key builder
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )"""
    storage = MemoryStorage()

    bot: Bot = Bot(token=config.bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage, events_isolation=SimpleEventIsolation())

    register_middleware(dp, db_middleware)
    register_middleware(dp, config_middleware)

    register_dialog(dp)
    register_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

    # Проверяет станые апдейты с учетом имеющихся хендлеров
    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
