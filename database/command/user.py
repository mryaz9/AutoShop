import datetime
from typing import Sequence

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


async def create_user(session: AsyncSession, user_id: int) -> None:
    """Create the User instance"""

    if not await is_user_exists(session, user_id):
        user = Users(id=user_id, register_time=datetime.datetime.now().date())
        session.add(user)
        await session.commit()


async def get_user(session: AsyncSession, user_id: int) -> Users:
    """Get User instance"""
    q = select(Users).where(Users.id == user_id)
    res = await session.execute(q)

    return res.scalar()


async def get_all_user(session: AsyncSession) -> Sequence[Users]:
    """Get User instance"""

    q = select(Users)
    res = await session.execute(q)

    return res.scalars().all()


async def create_admin(session: AsyncSession, user_id: int) -> bool:
    """Изменение флага админа"""

    user: Users = await get_user(session, user_id)
    if user:
        admin = not user.admin
        user.admin = admin
        session.add(user)
        await session.commit()
        return user.admin

    elif not user:
        await create_user(session, user_id)
        await create_admin(session, user_id)


async def add_admin(session: AsyncSession, user_id: int) -> bool:
    """Изменение флага админа на True"""

    user: Users = await get_user(session, user_id)
    if user:
        user.admin = True
        await session.commit()
        return user.admin

    elif not user:
        await create_user(session, user_id)
        await create_admin(session, user_id)


async def get_all_admin(session: AsyncSession) -> Sequence[Users]:
    """Get User instance"""

    q = select(Users).where(Users.admin)
    res = await session.execute(q)

    return res.scalars().all()
