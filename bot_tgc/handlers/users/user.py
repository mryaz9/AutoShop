import logging

from aiogram import Router
from aiogram.filters import CommandStart, ExceptionTypeFilter
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.api.exceptions import UnknownIntent, UnknownState
from sqlalchemy.ext.asyncio import AsyncSession

from bot_tgc.database.command.user import create_user
from bot_tgc.handlers.menu.main_windows import MainMenu

router = Router()


@router.message(CommandStart())
async def user_start(message: Message, dialog_manager: DialogManager, session: AsyncSession):
    database_user = await create_user(session, message.from_user.id)
    # TODO: Можно передать имя в диалог менеджер
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


async def on_unknown_intent(event, dialog_manager: DialogManager):
    """Example of handling UnknownIntent Error and starting new dialog."""
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        MainMenu.main_menu, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )


async def on_unknown_state(event, dialog_manager: DialogManager):
    """Example of handling UnknownState Error and starting new dialog."""
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        MainMenu.main_menu, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )


router.errors.register(
    on_unknown_intent,
    ExceptionTypeFilter(UnknownIntent),
)
router.errors.register(
    on_unknown_state,
    ExceptionTypeFilter(UnknownState),
)
