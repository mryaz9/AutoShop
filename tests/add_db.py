
import asyncio

from database.command.category import add_categories, add_subcategories
from database.init_database import create_db

categories = ['Услуги', 'Товары']
subcategories1 = ["Раскрутка", "Рассылка"]
subcategories2 = ["Телеграм", "Инстаграм", "Твиттер"]

item11 = ["Раскрутка тг", "раскрутка инсты"]
item21 = ["аккаунт"]


# Используем эту функцию, чтобы заполнить базу данных товарами
async def add_items():
    await create_db()
    for i in categories:
        await add_categories(category_name=i)

    for j in subcategories1:
        await add_subcategories(category_name=categories[0], subcategory_name=j)

    for j in subcategories2:
        await add_subcategories(category_name=categories[1], subcategory_name=j)

asyncio.run(add_items())
