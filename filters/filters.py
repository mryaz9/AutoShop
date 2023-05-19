from aiogram import types
from aiogram.enums import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from sqlalchemy.ext.asyncio import AsyncSession

from database.command.main_menu import get_menu
from database.command.user import get_user


async def is_admin(dialog_manager: DialogManager, session: AsyncSession, **kwargs):
    user = types.User.get_current()
    menu = await get_menu(session)

    admin = await get_user(session, user.id)
    admin = admin.admin

    data = {}

    if admin:
        data = {
            "admin": True
        }

    elif not admin:
        data = {
            "admin": False
        }

    data.update(photo=(MediaAttachment(ContentType.PHOTO, file_id=MediaId(menu.main_menu))
                       if menu.main_menu else None) if menu else None)
    return data
