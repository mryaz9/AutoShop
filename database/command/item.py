from typing import Sequence

from loguru import logger
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.subcategory import get_subcategory
from database.models import Item, ItemFiles
from schemas.admin import ItemModel


async def create_item(
    session: AsyncSession,
    item_obj: ItemModel,
) -> None:
    """
    Create the Item instance, shops are list of (shop_id, quantity), photos are list of (file_id)
    """

    item = Item(
        title=item_obj.title,
        description=item_obj.description,
        price=item_obj.price,
        photo=item_obj.photo,
        subcategory_id=item_obj.subcategory_id,
        quantity=item_obj.quantity
    )

    item_files_objects = []

    for files_id in item_obj.files:
        obj = ItemFiles(file_id=files_id)
        item_files_objects.append(obj)

    item.files.extend(item_files_objects)

    session.add(item)

    await session.commit()


async def update_item(session: AsyncSession, item_id: int, item_obj: ItemModel) -> None:
    """
    Create the Item instance, shops are list of (shop_id, quantity), photos are list of (file_id)
    """

    item = await get_item(session, item_id)

    if item_obj.title:
        item.title = item_obj.title

    if item_obj.description:
        item.description = item_obj.description

    if item_obj.price:
        item.price = item_obj.price

    if item_obj.photo:
        item.photo = item_obj.photo

    if item_obj.subcategory_id:
        item.subcategory_id = item_obj.subcategory_id

    if item_obj.quantity:
        item.quantity = item_obj.quantity

    if item_obj.files:
        item_files_objects = []

        for files_id in item_obj.files:
            obj = ItemFiles(file_id=files_id)
            item_files_objects.append(obj)

        item.files.extend(item_files_objects)

    session.add(item)

    await session.commit()


async def get_items_by_subcategory(session: AsyncSession, subcategory_id: int) -> Sequence[Item]:
    """Select items by category_id"""

    q = select(Item).where(Item.subcategory_id == subcategory_id)

    res = await session.execute(q)
    return res.scalars().all()


async def get_items_by_category_count(session: AsyncSession, subcategory_id: int) -> int:
    """Select COUNT items by category_id"""

    q = select(func.count(Item.id)).where(Item.subcategory_id == subcategory_id)

    res = await session.execute(q)

    return res.scalar()


async def get_items(session: AsyncSession) -> Sequence[Item]:
    """Select all items"""

    q = select(Item)

    res = await session.execute(q)

    return res.scalars().all()


async def get_item(session: AsyncSession, item_id: int) -> Item:
    """Get Item instance"""

    q = select(Item).where(Item.id == item_id)

    res = await session.execute(q)

    return res.scalar()


async def get_items_count(session: AsyncSession) -> int:
    """Select COUNT items"""

    q = select(func.count(Item.id))

    res = await session.execute(q)

    return res.scalar()


async def get_files(session: AsyncSession, item_id: int) -> Sequence[ItemFiles]:
    """Select COUNT items"""

    q = select(ItemFiles).where(ItemFiles.item_id == item_id)

    res = await session.execute(q)

    return res.scalars().all()


async def return_and_del_files(session: AsyncSession, item_id: int, amount: int) -> Sequence[ItemFiles]:
    """Select COUNT items"""

    q = select(ItemFiles).where(ItemFiles.item_id == item_id).limit(amount)
    res = await session.execute(q)

    result = []

    for i in res.scalars().all():
        res_id: int = i.id
        result.append(i.file_id)
        d = delete(ItemFiles).where(ItemFiles.id == res_id)
        await session.execute(d)

    await session.commit()

    return result


async def delete_item(session: AsyncSession, item_id: int) -> None:
    """Delete item by id"""

    q = delete(Item).where(Item.id == item_id)
    await session.execute(q)
    await session.commit()


async def add_files(session: AsyncSession, item_id: int, files: list) -> None:
    item = await get_item(session, item_id)

    item_files_objects = []

    for files_id in files:
        obj = ItemFiles(file_id=files_id, item_id=item.id)
        item_files_objects.append(obj)

    item.quantity += len(item_files_objects)

    session.add_all(item_files_objects)

    await session.commit()
