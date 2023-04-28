from aiogram import Router
from aiogram import F
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message

from lexicon.lexicon_ru import LEXICON_BUTTON_ADMIN, LEXICON_ADMIN, LEXICON_BUTTON_MAIN
from keyboards.kb_reply import create_reply_keyboard
from filters.filters import IsAdmin
from database.command import database_admin

router: Router = Router()
router.message.filter(IsAdmin())


@router.message(Command(commands=['admin']))
async def if_admins(message: Message):
    await message.answer(text=LEXICON_ADMIN['in_admin'],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_ADMIN.values())))


@router.message(Text(text=LEXICON_BUTTON_ADMIN["exit"]))
async def if_admins(message: Message):
    await message.answer(text=LEXICON_ADMIN['out_admin'],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))
