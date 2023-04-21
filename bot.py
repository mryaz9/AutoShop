import asyncio
import logging
from aiogram import Bot, Dispatcher

from database.database import Admin
from database.dataclassData import AdminData
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers, admin_handlers


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    Admin().set_data(AdminData(int(config.tg_bot.admin_ids[0]), config.tg_bot.admin_ids[1]))

    # Регистрируем роутер в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся адепты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
