import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Purchases


async def add_purchases(session: AsyncSession, purchases: Purchases):
    purchases = Purchases(buyer_id=purchases.buyer_id,
                          item_id=purchases.item_id,
                          amount=purchases.amount,
                          purchase_time=datetime.datetime.now()
                          )

    session.add(purchases)
    await session.commit()


async def get_purchases(session: AsyncSession, buyer_id: int) -> list[Purchases]:
    q = select(Purchases).where(Purchases.buyer_id == buyer_id)
    res = await session.execute(q)

    return res.scalar()
