from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.database import Admin


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        return user_id in Admin().get_data_user_id(user_id=user_id)
