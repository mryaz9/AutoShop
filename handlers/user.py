import logging

from aiogram import Router, types, F
from aiogram.filters import CommandStart, ExceptionTypeFilter, Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.api.exceptions import UnknownState, UnknownIntent

from database.command.database_user import add_new_user
from dialogs.bot_main_menu.states import BotMenu
from keyboards.reply import create_reply_keyboard
from lexicon.lexicon_ru import LEXICON_BUTTON_MAIN, LEXICON_MAIN

router = Router()


@router.message(CommandStart())
async def user_start(message: Message):
    database_user = await add_new_user()
    await message.answer(text=f"Привет {database_user.full_name}",
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_MAIN[message.text])


@router.message(F.text == LEXICON_BUTTON_MAIN["assortment"])
async def show_menu(message: types.Message, dialog_manager: DialogManager):
    # Выполним функцию, которая отправит пользователю кнопки с доступными категориями
    await dialog_manager.start(BotMenu.select_categories)


@router.message(F.text == LEXICON_BUTTON_MAIN["profile"])
async def button_profile(message: Message):
    await message.answer(text=LEXICON_MAIN["profile"])


@router.message(F.text == LEXICON_BUTTON_MAIN["️orders"])
async def button_orders(message: Message):
    await message.answer(text=LEXICON_MAIN["️orders"])


@router.message(F.text == LEXICON_BUTTON_MAIN["information"])
async def button_information(message: Message):
    await message.answer(text=LEXICON_MAIN["information"])


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

