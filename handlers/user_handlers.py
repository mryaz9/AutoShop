from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, callback_query

from lexicon.lexicon_ru import LEXICON, LEXICON_BUTTON_MAIN, LEXICON_NAME_CATALOG
from database import database
from keyboards.kb_main import create_reply_keyboard, create_inline_keyboard

router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    database_user = database.Users()
    if str(message.from_user.id) not in database_user.get_data_user_id(message.from_user.id):
        database_user.set_data(
            database.ColumnsData(message.from_user.id, message.from_user.username, 0, "None", "None"))

    await message.answer(text=LEXICON[message.text],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(F.text == LEXICON_BUTTON_MAIN["assortment"])
async def button_assortment(message: Message):
    await message.answer(text=LEXICON["assortment"],
                         reply_markup=create_inline_keyboard(list(LEXICON_NAME_CATALOG.values())))


@router.message(F.text == LEXICON_BUTTON_MAIN["profile"])
async def button_profile(message: Message):
    await message.answer(text=LEXICON["profile"])


@router.message(F.text == LEXICON_BUTTON_MAIN["️orders"])
async def button_orders(message: Message):
    await message.answer(text=LEXICON["️orders"])


@router.message(F.text == LEXICON_BUTTON_MAIN["information"])
async def button_information(message: Message):
    await message.answer(text=LEXICON["information"])


@router.callback_query(lambda x:x.data and x.data.startswith("set"))#TODO: Поменять на нормальный фильтр
async def catalog_callback(callback: types.CallbackQuery):
    replace = callback.data.replace("set", "")
    shop_list = database.Shop().get_data_catalog(replace)

    shop_list_format = []
    for i in shop_list:
        string = f"{i[0]}. {i[2]}  {i[3]}руб."
        shop_list_format.append(string)

    keyboard = create_inline_keyboard(shop_list_format)
    await callback.message.edit_text(text=replace, reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.text == 'back')
async def catalog_callback(callback: types.CallbackQuery):
    pass


@router.callback_query(F.text == 'to_main')
async def catalog_callback(callback: types.CallbackQuery):
    pass