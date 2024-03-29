# Функция для вывода товаров с РАЗНЫМИ категориями
from typing import Sequence

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Category
from schemas.admin import CategoryModel


async def get_categories(session: AsyncSession) -> Sequence[Category]:
    """Select all categories"""

    q = select(Category)

    res = await session.execute(q)

    return res.scalars().all()


async def get_categories_count(session: AsyncSession) -> int:
    """Get count of categories"""

    q = select(func.count(Category.id))

    res = await session.execute(q)

    return res.scalar()


async def get_category(session: AsyncSession, category_id: int) -> Category:
    """Get Category instance"""

    q = select(Category).where(Category.id == category_id)
    res = await session.execute(q)

    return res.scalar()


async def create_category(session: AsyncSession, category_obj: CategoryModel) -> None:
    """Create the Category instance"""

    category = Category(title=category_obj.title, photo=category_obj.photo)

    session.add(category)
    await session.commit()


async def update_category(session: AsyncSession, category_id: int, category_obj: CategoryModel) -> None:
    """Updata the Category instance"""

    category = await get_category(session, category_id)

    if category_obj.title:
        category.title = category_obj.title

    if category_obj.photo:
        category.photo = category_obj.photo

    session.add(category)
    await session.commit()


async def delete_category(session: AsyncSession, category_id: int) -> None:
    """Delete category by id"""

    q = delete(Category).where(Category.id == category_id)
    await session.execute(q)

    await session.commit()
