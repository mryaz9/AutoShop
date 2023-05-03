import logging

from aiogram import Router
from aiogram.filters import CommandStart, ExceptionTypeFilter
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode, setup_dialogs
from aiogram_dialog.api.exceptions import UnknownState, UnknownIntent

from dialogs.bot_main_menu.states import BotMenu

router = Router()


@router.message(CommandStart())
async def user_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(BotMenu.select_categories)


async def on_unknown_intent(event, dialog_manager: DialogManager):
    """Example of handling UnknownIntent Error and starting new dialog."""
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        BotMenu.select_categories, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )


async def on_unknown_state(event, dialog_manager: DialogManager):
    """Example of handling UnknownState Error and starting new dialog."""
    logging.error("Restarting dialog: %s", event.exception)
    await dialog_manager.start(
        BotMenu.select_categories, mode=StartMode.RESET_STACK, show_mode=ShowMode.SEND,
    )

router.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )
router.errors.register(
        on_unknown_state,
        ExceptionTypeFilter(UnknownState),
    )

