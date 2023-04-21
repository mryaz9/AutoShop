from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message


from lexicon.lexicon_ru import LEXICON
from database import database
from keyboards.kb_main import create_keyboard_main

router: Router = Router()
database_user = database.Users()


@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in database_user.get_data_user_id(message.from_user.id):
        database_user.set_data(database.ColumnsData(message.from_user.id, message.from_user.username, 0, "None", "None"))

    await message.answer(text=LEXICON[message.text], reply_markup=create_keyboard_main())


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


