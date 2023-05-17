import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.item import get_item, get_service
from database.command.user import get_user
from database.models import Order


async def add_order(session: AsyncSession, order_obj: Order):
    order = Order()

    if order_obj.item_id:
        item = await get_item(session, order_obj.item_id)
        order.item = item

    if order_obj.quantity:
        order.quantity = order_obj.quantity

    if order_obj.service_id:
        service = await get_service(session, order_obj.service_id)
        order.service = service

    user = await get_user(session, order_obj.user_id)

    order.user = user
    order.summ = order_obj.summ

    if order_obj.item_id:
        item_shop = await get_item(session, order_obj.item_id)
        item_shop.quantity = item_shop.quantity - order.quantity

    session.add(order)
    await session.commit()

    return order


async def get_purchases(session: AsyncSession, buyer_id: int) -> Sequence[Order]:
    q = select(Order).where(Order.buyer_id == buyer_id)
    res = await session.execute(q)

    return res.scalars().all()
