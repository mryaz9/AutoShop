import logging

from aiogram import Router, types, F
from aiogram.filters import CommandStart, ExceptionTypeFilter, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.api.exceptions import UnknownState, UnknownIntent

from database.command.user import add_new_user
from dialogs.assortiment.states import BotMenu
from dialogs.main_menu.windows import MainMenu
from lexicon.lexicon_ru import LEXICON_BUTTON_MAIN, LEXICON_MAIN

router = Router()


@router.message(CommandStart())
async def user_start(message: Message, dialog_manager: DialogManager):
    database_user = await add_new_user()  # TODO: Можно передать имя в диалог менеджер
    await dialog_manager.start(MainMenu.main_menu, mode=StartMode.RESET_STACK)


'''
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

'''