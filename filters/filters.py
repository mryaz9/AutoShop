from aiogram.filters import BaseFilter


class IsAdmin(BaseFilter):
    async def __call__(self) -> bool:
        return