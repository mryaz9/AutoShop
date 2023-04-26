from typing import List

from sqlalchemy import and_

from database.init_database import db
from database.models import Items


# Функция для создания нового товара в базе данных. Принимает все возможные аргументы, прописанные в Item
async def add_item(self, **kwargs):
    new_item = await Items(**kwargs).create()
    return new_item


# Функция для вывода товаров с РАЗНЫМИ категориями
async def get_categories() -> List[Items]:
    return await Items.query.distinct(Items.category_name).gino.all()


# Функция для вывода товаров с РАЗНЫМИ подкатегориями в выбранной категории
async def get_subcategories(category) -> List[Items]:
    return await Items.query.distinct(Items.subcategory_name).where(Items.category_code == category).gino.all()


# Функция для подсчета товаров с выбранными категориями и подкатегориями
async def count_items(category_code, subcategory_code=None):
    # Прописываем условия для вывода (категория товара равняется выбранной категории)
    conditions = [Items.category_code == category_code]

    # Если передали подкатегорию, то добавляем ее в условие
    if subcategory_code:
        conditions.append(Items.subcategory_code == subcategory_code)

    # Функция подсчета товаров с указанными условиями
    total = await db.select([db.func.count()]).where(
        and_(*conditions)
    ).gino.scalar()
    return total


# Функция вывода всех товаров, которые есть в переданных категории и подкатегории
async def get_items(category_code, subcategory_code) -> List[Items]:
    item = await Items.query.where(
        and_(Items.category_code == category_code,
             Items.subcategory_code == subcategory_code)
    ).gino.all()
    return item


# Функция для получения объекта товара по его айди
async def get_item(item_id) -> Items:
    item = await Items.query.where(Items.id == item_id).gino.first()
    return item
