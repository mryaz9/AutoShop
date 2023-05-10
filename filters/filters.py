from aiogram import types
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.common import Whenable

from database.command import admin


async def is_admin(dialog_manager: DialogManager, **kwargs):
    user = types.User.get_current()
    admin1 = await admin.get_admin(user.id)
    if admin1 is not None:
        data = {
            "admin": True
        }
        return data

    elif admin1 is None:
        data = {
            "admin": False
        }
        return data
