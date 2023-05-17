from typing import Sequence

from loguru import logger
from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.subcategory import get_subcategory
from database.models import Item, ItemFiles, Service
from schemas.admin import ItemModel


async def create_item(
    session: AsyncSession,
    item_obj: ItemModel,
) -> None:
    """
    Create the Item instance, shops are list of (shop_id, quantity), photos are list of (file_id)
    """

    item = Item(
        name=item_obj.name,
        description=item_obj.description,
        price=item_obj.price,
        photo=item_obj.photo,
        subcategory_id=item_obj.subcategory_id
    )

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


async def hide_item(session: AsyncSession, item_id: int) -> None:
    """Hide item by id"""

    item = await get_item(session, item_id)
    show = not item.show
    item.show = show

    await session.commit()


async def delete_item(session: AsyncSession, item_id: int) -> None:
    """Delete item by id"""

    q = delete(Item).where(Item.id == item_id)
    await session.execute(q)

    await session.commit()


async def create_service(session: AsyncSession, service_obj: ItemModel) -> Service:
    """Create the ServiceCategory instance"""

    service = Service(title=service_obj.title, description=service_obj.description, price=service_obj.price)

    subcategory = await get_subcategory(session, service_obj.subcategory_id)
    service.subcategory = subcategory

    session.add(service)

    await session.commit()

    return service


async def get_service(session: AsyncSession, service_id: int) -> Service:
    """Get Service instance"""

    q = select(Service).where(Service.id == service_id)
    res = await session.execute(q)

    return res.scalar()
