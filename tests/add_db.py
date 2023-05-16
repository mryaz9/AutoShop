import asyncio

from database.command.category import add_categories, add_subcategories
from database.command.item import add_item
from database.__init__ import create_db
from database.models import Category, SubCategory, Items

categories = [
    {
        'name': 'Электроника',
        'subcategories': [
            dict(name='Смартфоны', products=[
                {'name': 'Samsung Galaxy S21', 'price': 80000},
                {'name': 'iPhone 12', 'price': 90000},
                {'name': 'Xiaomi Mi 11', 'price': 50000},
                {'name': 'OnePlus 9', 'price': 60000},
                {'name': 'iPhone 11', 'price': 90000},
                {'name': 'iPhone 10', 'price': 80000},
                {'name': 'iPhone 9', 'price': 70000},
                {'name': 'iPhone 8', 'price': 60000},
                {'name': 'iPhone 7', 'price': 50000},
                {'name': 'iPhone 6', 'price': 40000},
                {'name': 'iPhone 5', 'price': 30000},
                {'name': 'iPhone 4', 'price': 20000},

            ]),
            {
                'name': 'Ноутбуки',
                'products': [
                    {'name': 'MacBook Pro', 'price': 150000},
                    {'name': 'Dell XPS', 'price': 120000},
                    {'name': 'Lenovo ThinkPad', 'price': 90000}
                ]
            }
        ]
    },
    {
        'name': 'Одежда',
        'subcategories': [
            {
                'name': 'Мужская одежда',
                'products': [
                    {'name': 'Футболка', 'price': 2000},
                    {'name': 'Рубашка', 'price': 5000},
                    {'name': 'Джинсы', 'price': 4000}
                ]
            },
            {
                'name': 'Женская одежда',
                'products': [
                    {'name': 'Платье', 'price': 10000},
                    {'name': 'Блузка', 'price': 5000},
                    {'name': 'Джинсы', 'price': 4000}
                ]
            }
        ]
    }
]


# Используем эту функцию, чтобы заполнить базу данных товарами
async def add_items():
    await create_db()
    i = 0
    j = 0
    for cat in categories:
        await add_categories(Category(category_name=cat.get("name")))
        subcategory_name = cat.get("subcategories")
        i += 1
        for sub in subcategory_name:
            await add_subcategories(SubCategory(subcategory_name=sub.get("name"), category_id=i))
            item_name = sub.get("products")
            j += 1
            for item in item_name:
                await add_item(Items(subcategory_id=j, name=item.get("name"), price=item.get("price")))


asyncio.run(add_items())
