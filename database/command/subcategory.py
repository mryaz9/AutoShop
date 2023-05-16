# Функция для вывода товаров с РАЗНЫМИ подкатегориями
from typing import Sequence

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import SubCategory
from schemas.admin import SubCategoryModel


async def get_subcategories(session: AsyncSession, category_id: int) -> Sequence[SubCategory]:
    """Select all subcategories"""

    q = select(SubCategory).where(SubCategory.category_id == category_id)

    res = await session.execute(q)

    return res.scalars().all()


async def get_subcategories_count(session: AsyncSession) -> int:
    """Get count of subcategories"""

    q = select(func.count(SubCategory.id))

    res = await session.execute(q)

    return res.scalar()


async def get_subcategory(session: AsyncSession, subcategory_id: int) -> SubCategory:
    """Get SubCategory instance"""

    q = select(SubCategory).where(SubCategory.id == subcategory_id)
    res = await session.execute(q)

    return res.scalar()


async def create_subcategory(session: AsyncSession, subcategory_obj: SubCategoryModel) -> None:
    """Create the SubCategory instance"""

    category = SubCategory(title=subcategory_obj.title, photo=subcategory_obj.photo,
                           category_id=subcategory_obj.category_id)

    session.add(category)
    await session.commit()


async def delete_subcategory(session: AsyncSession, subcategory_id: int) -> None:
    """Delete subcategory by id"""

    q = delete(SubCategory).where(SubCategory.id == subcategory_id)
    await session.execute(q)

    await session.commit()
