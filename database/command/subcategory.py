# Функция для вывода товаров с РАЗНЫМИ подкатегориями
from typing import Sequence

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.category import get_category
from database.models import SubCategory
from schemas.admin import SubCategoryModel


async def get_subcategories(session: AsyncSession, category_id: int) -> Sequence[SubCategory]:
    """Select all subcategories"""

    q = select(SubCategory).where(SubCategory.category_id == category_id)

    res = await session.execute(q)

    return res.scalars().all()


async def get_subcategories_count(session: AsyncSession, category_id: int) -> int:
    """Get count of subcategories"""

    q = select(func.count(SubCategory.id)).where(SubCategory.category_id == category_id)

    res = await session.execute(q)

    return res.scalar()


async def get_subcategory(session: AsyncSession, subcategory_id: int) -> SubCategory:
    """Get SubCategory instance"""

    q = select(SubCategory).where(SubCategory.id == subcategory_id)
    res = await session.execute(q)

    return res.scalar()


async def create_subcategory(session: AsyncSession, subcategory_obj: SubCategoryModel) -> None:
    """Create the SubCategory instance"""

    subcategory = SubCategory(title=subcategory_obj.title, photo=subcategory_obj.photo,
                              category_id=subcategory_obj.category_id)

    category = await get_category(session, subcategory_obj.category_id)

    subcategory.category = category

    session.add(subcategory)
    await session.commit()


async def update_subcategory(session: AsyncSession, subcategory_id: int, subcategory_obj: SubCategoryModel) -> None:
    """Update the Category instance"""

    subcategory = await get_subcategory(session, subcategory_id)

    if subcategory_obj.title:
        subcategory.title = subcategory_obj.title

    if subcategory_obj.photo:
        subcategory.photo = subcategory_obj.photo

    if subcategory_obj.category_id:
        category = await get_category(session, subcategory_obj.category_id)
        subcategory.category = category

    session.add(subcategory)
    await session.commit()


async def delete_subcategory(session: AsyncSession, subcategory_id: int) -> None:
    """Delete subcategory by id"""

    q = delete(SubCategory).where(SubCategory.id == subcategory_id)
    await session.execute(q)

    await session.commit()
