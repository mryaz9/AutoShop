# Функция для вывода товаров с РАЗНЫМИ категориями
from database.models import Category, SubCategory


async def add_categories(**kwargs):
    new_item = await Category(**kwargs).create()
    return new_item


async def get_categories() -> list[Category]:
    return await Category.query.distinct(Category.category_name).gino.all()


async def add_subcategories(**kwargs):
    new_item = await SubCategory(**kwargs).create()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> list[SubCategory]:
    return await SubCategory.query.distinct(SubCategory.subcategory_name).where(
        SubCategory.category_id == category).gino.all()
