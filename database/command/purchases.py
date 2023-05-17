import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Order


async def add_purchases(session: AsyncSession, purchases: Order):
    purchases = Order(buyer_id=purchases.buyer_id,
                      item_id=purchases.item_id,
                      amount=purchases.amount,
                      purchase_time=datetime.datetime.now()
                      )

    session.add(purchases)
    await session.commit()


async def get_purchases(session: AsyncSession, buyer_id: int) -> Sequence[Order]:
    q = select(Order).where(Order.buyer_id == buyer_id)
    res = await session.execute(q)

    return res.scalars().all()
