from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.filters import Command, Text, StateFilter
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)

from filters import filters
from keyboards import kb_inline
from database.command import database_item
from lexicon.lexicon_ru import LEXICON_BUTTON_ADMIN, LEXICON_FSM_SHOP

router: Router = Router()


# .message.filter(filters.IsAdmin())


class FSMFillCard(StatesGroup):
    fill_category_code = State()
    fill_category = State()
    fill_subcategory_code = State()
    fill_subcategory = State()
    fill_name = State()
    fill_photo = State()
    fill_price = State()
    fill_time_action = State()
    fill_description = State()


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_FSM_SHOP["cancel"])
    await state.clear()


@router.message(Text(text=LEXICON_BUTTON_ADMIN["add_assortment"]), StateFilter(default_state))
async def process_fill_command(message: Message, state: FSMContext):
    markup = kb_inline.create_inline_keyboard(database_item.get_categories())
    await message.answer(text=LEXICON_FSM_SHOP["category"], reply_markup=markup)
    await state.set_state(FSMFillCard.fill_category_code)


@router.callback_query(StateFilter(FSMFillCard.fill_category),
                       Text(text=list(LEXICON_FSM_SHOP.values())))
async def process_fill_catalog(callback: CallbackQuery, state: FSMContext):
    await state.update_data(catalog=callback.data)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["name"])
    await state.set_state(FSMFillCard.fill_name)


@router.message(StateFilter(FSMFillCard.fill_name), F.text)
async def process_fill_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["price"])
    await state.set_state(FSMFillCard.fill_price)


@router.message(StateFilter(FSMFillCard.fill_price), F.text.isdigit())
async def process_fill_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["time_action"])
    await state.set_state(FSMFillCard.fill_time_action)


@router.message(StateFilter(FSMFillCard.fill_time_action), F.text.isdigit())
async def process_fill_time_action(message: Message, state: FSMContext):
    await state.update_data(time_action=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["description"])
    await state.set_state(FSMFillCard.fill_description)


@router.message(StateFilter(FSMFillCard.fill_description), F.text)
async def process_fill_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    # keyboard = view_inline_keyboard(["Да", "Нет"])
    data = await state.get_data()
    await message.answer(text=f"{LEXICON_FSM_SHOP['done']} {[*data.values()]}", reply_markup=keyboard)


@router.callback_query(StateFilter(FSMFillCard.fill_description),
                       Text(text=["Да", "Нет"]))
async def process_check(callback: CallbackQuery, state: FSMContext):
    if callback.data == "Да":
        data = await state.get_data()
        # Shop().set_data(ShopData(*data.values()))
        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_yes"], show_alert=True)

    elif callback.data == "Нет":
        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_no"], show_alert=True)

    await callback.message.delete()


@router.message(~StateFilter(default_state))
async def warning_not(message: Message):
    await message.answer(text=LEXICON_FSM_SHOP["unknown"])
