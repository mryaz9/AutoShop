from gino import Gino
from gino.schema import GinoSchemaVisitor
from config_data.config import Config, load_config

config: Config = load_config()
db = Gino()

POSTGRES_URI = f"postgresql://{config.tg_bot.PGUSER}:{config.tg_bot.PGPASSWORD}@{config.tg_bot.ip}/{config.tg_bot.DATABASE}"


async def create_db():
    # Устанавливаем связь с базой данных
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor

    # Создаем таблицы
    #await db.gino.drop_all()
    await db.gino.create_all()
