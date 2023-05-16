import datetime
from aiogram import types
from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Users


async def add_balance(session: AsyncSession, amount: float, user_id: int):
    user = await get_user(session, user_id)
    old_balance = user.balance
    balance = old_balance+amount
    user.balance = balance

    session.add(user)
    await session.commit()


async def reduce_balance(session: AsyncSession, amount: float, user_id: int):
    user = await get_user(session, user_id)
    old_balance = user.balance
    balance = old_balance-amount
    user.balance = balance

    session.add(user)
    await session.commit()


async def is_user_exists(session: AsyncSession, user_id: int) -> bool:
    """Checks for the presence of a user with the passed id"""

    q = select(exists().where(Users.id == user_id))
    res = await session.execute(q)
    return res.scalar()


async def create_user(session: AsyncSession, user_id: int, register_time: datetime.datetime.date) -> None:
    """Create the User instance"""

    user = Users(id=user_id, register_time=register_time)
    session.add(user)
    await session.commit()


async def get_user(session: AsyncSession, user_id: int) -> Users:
    """Get User instance"""

    q = select(Users).where(Users.id == user_id)
    res = await session.execute(q)

    return res.scalar()


async def create_admin(session: AsyncSession, user_id: int) -> None:
    """Изменение флага админа"""

    user: Users = await get_user(session, user_id)
    admin = not user.admin
    user.admin = admin
    session.add(user)
    await session.commit()
