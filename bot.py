import asyncio
from loguru import logger
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis

from keyboards.main_menu import set_main_menu
from utils.notify_admin import startup, shutdown

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers, admin_handlers
from FSM import FSM_shop_card
from database.init_database import create_db
from database.command.database_admin import add_new_admin


# Функция конфигурирования и запуска бота
@logger.catch
async def main():
    # Конфигурируем логирование


    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    redis: Redis = Redis(host=config.tg_bot.ip)
    storage: RedisStorage = RedisStorage(redis=redis)
    await create_db()
    await add_new_admin(int(config.tg_bot.admin_ids[0]))


    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher(storage=storage)

    # await set_main_menu(bot)

    # Регистрируем роутер в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(FSM_shop_card.router)

    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся адепты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)

    # dp.startup.register(startup)
    # dp.shutdown.register(shutdown)

    await dp.start_polling(bot)


    #Проверяет станые апдейты с учетом имеющихся хендлеров
    #await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
