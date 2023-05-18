import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.item import get_item
from database.command.user import get_user
from database.models import Order, UserItem


async def add_order(session: AsyncSession, order_obj: Order):
    order = Order()

    if order_obj.item_id:
        item = await get_item(session, order_obj.item_id)
        order.item = item

    if order_obj.quantity:
        order.quantity = order_obj.quantity

    user = await get_user(session, order_obj.user_id)

    order.user = user
    order.summ = order_obj.summ

    session.add(order)
    await session.commit()

    return order


async def get_purchases(session: AsyncSession, buyer_id: int) -> Sequence[Order]:
    q = select(Order).where(Order.buyer_id == buyer_id)
    res = await session.execute(q)

    return res.scalars().all()


async def add_user_item(session: AsyncSession, user_item_obj: UserItem):
    user_item = UserItem()

    if user_item_obj.item_id:
        item = await get_item(session, user_item_obj.item_id)
        user_item.item = item

    if user_item_obj.quantity:
        user_item.quantity = user_item_obj.quantity

    user = await get_user(session, user_item_obj.user_id)

    user_item.user = user

    session.add(user_item)
    await session.commit()

    return user_item
