from aiogram import types

from database.init_database import db
from database.models import Users


async def get_user(user_id):
    user = await Users.query.where(Users.user_id == user_id).gino.first()
    return user


async def add_new_user():
    user = types.User.get_current()
    old_user = await get_user(user.id)
    if old_user:
        return old_user
    new_user = Users()
    new_user.user_id = user.id
    new_user.username = user.username
    new_user.full_name = user.full_name

    await new_user.create()
    return new_user


async def count_users() -> int:
    total = await db.func.count(Users.id).gino.scalar()
    return total
