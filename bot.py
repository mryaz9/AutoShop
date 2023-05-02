import asyncio

from aiogram_dialog import setup_dialogs
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis, DefaultKeyBuilder

from handlers import user
from utils.notify_admin import startup, shutdown
from config_data.config import Config, load_config

from database.init_database import create_db
from database.command.database_admin import add_new_admin


# Функция конфигурирования и запуска бота
@logger.catch
async def main():
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    storage = RedisStorage(
        Redis(host=config.tg_bot.ip),
        # in case of redis you need to configure key builder
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )
    await create_db()
    await add_new_admin(int(config.tg_bot.admin_ids[0]))

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    # Пропускаем накопившиеся адепты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    setup_dialogs(dp)
    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)

    dp.include_router(user.router)

    await dp.start_polling(bot)

    # Проверяет старые апдейты с учетом имеющихся хендлеров
    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
