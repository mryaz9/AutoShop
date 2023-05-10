from loguru import logger
from sqlalchemy import and_

from database.init_database import db
from database.models import Items, Category, SubCategory


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_item(items: Items):
    new_item = await items.create()
    return new_item


# Функция для подсчета товаров с выбранными категориями и подкатегориями
async def count_items(category_id, subcategory_id=None):
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = [Category.id == category_id]

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_id:
        conditions.append(SubCategory.id == subcategory_id)

    # Функция подсчета товаров с указанными условиями
    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(subcategory_id) -> list[Items]:
    item = await Items.query.distinct(Items.name).where(Items.subcategory_id == subcategory_id).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Items:
    item = await Items.query.where(Items.id == item_id).gino.first()
    return item
