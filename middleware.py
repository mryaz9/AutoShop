from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from sqlalchemy.orm import async_sessionmaker

from config.config import Config


class DBSessionMiddleware(BaseMiddleware):
    """Middleware that pass the database session to the handler"""

    def __init__(self, async_sessionmaker: async_sessionmaker) -> None:
        self.sessionmaker = async_sessionmaker

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        async with self.sessionmaker() as session:
            data["db_session"] = session

            result = await handler(event, data)
            return result


class ConfigMiddleware(BaseMiddleware):
    """Middleware that pass the config_loader.Config object to the handler"""

    def __init__(self, config: Config) -> None:
        self.config = config

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:

        data["config"] = self.config
        result = await handler(event, data)
        return result
