from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from aiogram import F

from lexicon.lexicon_ru import LEXICON, LEXICON_BUTTON_MAIN
from database import database
from keyboards.kb_main import create_reply_keyboard

router: Router = Router()
database_user = database.Users()


@router.message(CommandStart())
async def process_start_command(message: Message):
    if message.from_user.id not in database_user.get_data_user_id(message.from_user.id):
        database_user.set_data(
            database.ColumnsData(message.from_user.id, message.from_user.username, 0, "None", "None"))

    await message.answer(text=LEXICON[message.text],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(F.text == LEXICON_BUTTON_MAIN["assortment"])
async def button_assortment(message: Message):
    await message.answer(text=LEXICON["assortment"])


@router.message(F.text == LEXICON_BUTTON_MAIN["profile"])
async def button_profile(message: Message):
    await message.answer(text=LEXICON["profile"])


@router.message(F.text == LEXICON_BUTTON_MAIN["️orders"])
async def button_️orders(message: Message):
    await message.answer(text=LEXICON["️orders"])


@router.message(F.text == LEXICON_BUTTON_MAIN["information"])
async def button_information(message: Message):
    await message.answer(text=LEXICON["information"])
