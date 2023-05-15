from aiogram import types

from database.init_database import db
from database.models import Admins


async def get_admin(user_id):
    user = await Admins.query.where(Admins.user_id == user_id).gino.first()
    return user


async def get_all_admin():
    return await Admins.query.distinct(Admins.user_id).gino.all()


async def add_new_admin(id_user: int):
    old_user = await get_admin(id_user)
    if old_user:
        return old_user
    new_user = Admins()
    new_user.user_id = id_user

    await new_user.create()
    return new_user


async def count_admin() -> int:
    total = await db.func.count(Admins.id).gino.scalar()
    return total
