from typing import Sequence

from loguru import logger
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.subcategory import get_subcategory
from database.models import Items, ItemFiles
from schemas.admin import ItemModel


async def create_item(
    session: AsyncSession,
    item_obj: ItemModel,
) -> None:
    """
    Create the Item instance, shops are list of (shop_id, quantity), photos are list of (file_id)
    """

    subcategory = await get_subcategory(session, item_obj.subcategory_id)

    item = Items(
        name=item_obj.name,
        description=item_obj.description,
        price=item_obj.price,
        photo=item_obj.photo
    )

    item.subcategory_id = subcategory

    item_files_objects = []

    for files_id in item_obj.files:
        obj = ItemFiles(file_id=files_id)
        item_files_objects.append(obj)

    item.files.extend(item_files_objects)

    session.add(item)

    await session.commit()


async def get_items_by_subcategory(session: AsyncSession, subcategory_id: int) -> Sequence[Items]:
    """Select items by category_id"""

    q = select(Items).where(Items.subcategory_id == subcategory_id)

    res = await session.execute(q)

    return res.scalars().all()


async def get_items_by_category_count(session: AsyncSession, subcategory_id: int) -> int:
    """Select COUNT items by category_id"""

    q = select(func.count(Items.id)).where(Items.subcategory_id == subcategory_id)

    res = await session.execute(q)

    return res.scalar()


async def get_items(session: AsyncSession) -> Sequence[Items]:
    """Select all items"""

    q = select(Items)

    res = await session.execute(q)

    return res.scalars().all()


async def get_item(session: AsyncSession, item_id: int) -> Items:
    """Get Item instance"""

    q = select(Items).where(Items.id == item_id)

    res = await session.execute(q)

    return res.scalar()


async def get_items_count(session: AsyncSession) -> int:
    """Select COUNT items"""

    q = select(func.count(Items.id))

    res = await session.execute(q)

    return res.scalar()


async def hide_item(session: AsyncSession, item_id: int) -> None:
    """Hide item by id"""

    item = await get_item(session, item_id)
    show = not item.show
    item.show = show

    await session.commit()


async def delete_item(session: AsyncSession, item_id: int) -> None:
    """Delete item by id"""

    q = delete(Items).where(Items.id == item_id)
    await session.execute(q)

    await session.commit()
