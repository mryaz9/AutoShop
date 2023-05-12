import datetime

from aiogram import types

from database.init_database import db
from database.models import Users


async def get_user(user_id) -> Users:
    user = await Users.query.where(Users.user_id == user_id).gino.first()
    return user


async def get_all_user():
    return await Users.query.distinct(Users.user_id).gino.all()


async def add_new_user() -> Users:
    user = types.User.get_current()
    old_user = await get_user(user.id)
    if old_user:
        return old_user
    new_user: Users = Users()
    new_user.user_id = user.id
    new_user.username = user.username
    new_user.full_name = user.full_name
    new_user.register_time = datetime.datetime.now()

    await new_user.create()
    return new_user


async def count_users() -> int:
    total = await db.func.count(Users.id).gino.scalar()
    return total


async def add_balance(amount: float, user_id: int):
    user = await get_user(user_id)
    old_balance = user.balance
    balance = amount+old_balance
    user.balance = balance
    await user.update(balance=balance).apply()
    await db.gino.create_all()


async def reduce_balance(amount: float, user_id: int):
    user = await get_user(user_id)
    old_balance = user.balance
    balance = old_balance-amount
    user.balance = balance
    await user.update(balance=balance).apply()
    await db.gino.create_all()

