from aiogram_dialog import DialogManager
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.user import get_all_admin


async def getter_admins(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    db_admins = await get_all_admin(session)
    data = {
        "admins": [
            (admin, admin.id)
            for admin in db_admins
        ]
    }
    return data
