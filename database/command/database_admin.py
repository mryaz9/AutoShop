from aiogram import types

from database.init_database import db
from database.models import Admins


async def get_admin(user_id):
    user = await Admins.query.where(Admins.user_id == user_id).gino.first()
    return user


async def add_new_admin():
    user = types.User.get_current()
    old_user = await get_admin(user.id)
    if old_user:
        return old_user
    new_user = Admins()
    new_user.user_id = user.id
    new_user.username = user.username

    await new_user.create()
    return new_user


async def count_admin() -> int:
    total = await db.func.count(Admins.id).gino.scalar()
    return total