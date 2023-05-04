from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram_dialog import DialogManager

from dialogs.admin.states import AdminMenu
from dialogs.assortiment.states import BotMenu
from filters.filters import IsAdmin
from lexicon.lexicon_ru import LEXICON_ADMIN, LEXICON_BUTTON_ADMIN, LEXICON_BUTTON_MAIN

router: Router = Router()
router.message.filter(IsAdmin())

'''
@router.message(Command(commands=['admin']))
async def if_admins(message: Message, dialog_manager: DialogManager):
    await message.answer(text=LEXICON_ADMIN['in_admin'],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_ADMIN.values())))


@router.message(Text(text=LEXICON_BUTTON_ADMIN["exit"]))
async def admins_exit(message: Message):
    await message.answer(text=LEXICON_ADMIN['out_admin'],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))


@router.message(Text(text=LEXICON_BUTTON_ADMIN["add_assortment"]))
async def admins_add(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AdminMenu.select_categories)



'''