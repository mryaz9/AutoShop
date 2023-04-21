from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message

from lexicon.lexicon_ru import LEXICON
from filters.filters import IsAdmin

router: Router = Router()


@router.message(IsAdmin() and Command(commands=['admin']))
async def answer_if_admins_update(message: Message):
    await message.answer(text='Вы админ')
