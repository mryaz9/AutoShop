from aiogram import types
from aiogram_dialog import DialogManager
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.user import get_user


async def is_admin(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    user = types.User.get_current()
    admin = await get_user(session, user.id)
    admin = admin.admin

    if admin is not None:
        data = {
            "admin": True
        }
        return data

    elif admin is None:
        data = {
            "admin": False
        }
        return data
