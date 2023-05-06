from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.command import admin


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        admin = await database_admin.get_admin(user_id)
        if admin:
            return True
