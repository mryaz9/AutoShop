from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon_ru import LEXICON

from database import database

router: Router = Router()
database_user = database.Users()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])
    if message.from_user.id not in database_user.get_data_user_id(message.from_user.id):
        database_user.set_data(database.ColumnsUserDC(message.from_user.id, message.from_user.username, 0, "None", "None"))



