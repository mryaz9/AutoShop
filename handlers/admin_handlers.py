from aiogram import Router
from aiogram import F
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message

from lexicon.lexicon_ru import LEXICON_BUTTON_ADMIN, LEXICON
from keyboards.kb_reply import create_reply_keyboard
from filters.filters import IsAdmin
from database.command import database_admin


router: Router = Router()
#router.message.filter(IsAdmin())


@router.message(Command(commands=['admin']))
async def if_admins(message: Message):
    await message.answer(text='Режим администратора',
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_ADMIN.values())))
