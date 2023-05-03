import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder

from dialogs.bot_main_menu import bot_menu_dialogs
from handlers import user
from utils.notify_admin import startup, shutdown
from config_data.config import Config, load_config

from database.init_database import create_db
from database.command.database_admin import add_new_admin


def register_all_dialog(dp):
    dialog = bot_menu_dialogs()
    for i in dialog:
        dp.include_router(i)
    setup_dialogs(dp)


def register_all_handlers(dp):
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)
    dp.include_router(user.router)


async def creating_db(config):
    await create_db()
    await add_new_admin(int(config.tg_bot.admin_ids[0]))


# Функция конфигурирования и запуска бота
#@logger.catch
async def main():
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
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
    asyncio.run(main())
