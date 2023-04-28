from aiogram import Router, types
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.filters import Command, Text, StateFilter, or_f, and_f
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.command.database_item import add_item
from filters import filters
from keyboards import kb_inline
from database.command import database_item
from keyboards.kb_inline import MenuCD, create_inline_keyboard, add_new_category, add_new_subcategory
from keyboards.kb_reply import create_reply_keyboard
from lexicon.lexicon_ru import LEXICON_BUTTON_ADMIN, LEXICON_FSM_SHOP, LEXICON_ADMIN

router: Router = Router()

router.message.filter(filters.IsAdmin())


class FSMFillCard(StatesGroup):
    category_code = State()
    subcategory_code = State()

    new_category_code = State()
    new_category_name = State()
    new_subcategory_code = State()
    new_subcategory_name = State()

    name = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()


@router.message(or_f(Command(commands='cancel'), Text(text=LEXICON_FSM_SHOP['cancel'])), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(text=LEXICON_FSM_SHOP["cancel"])
    await state.clear()
    await message.answer(text=LEXICON_ADMIN['in_admin'],
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_ADMIN.values())))


@router.message(Text(text=LEXICON_BUTTON_ADMIN["add_assortment"]), StateFilter(default_state))
async def process_fill_command(message: Message, state: FSMContext):
    markup = add_new_category(await kb_inline.categories_keyboard()).as_markup()

    await message.answer(text=LEXICON_FSM_SHOP["start"],
                         reply_markup=create_reply_keyboard(list([LEXICON_FSM_SHOP['cancel']])))

    await message.answer(text=LEXICON_FSM_SHOP["category_code"], reply_markup=markup)
    await state.set_state(FSMFillCard.category_code)


@router.callback_query(StateFilter(FSMFillCard.category_code), MenuCD.filter())
async def process_fill_category(callback: CallbackQuery, state: FSMContext):
    category_code = MenuCD.unpack(callback.data).category_code
    category_name = MenuCD.unpack(callback.data).category_name
    await state.update_data(category_code=category_code, category_name=category_name)

    markup = add_new_subcategory(await kb_inline.subcategories_keyboard(category_code)).as_markup()
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["subcategory_code"], reply_markup=markup)
    await state.set_state(FSMFillCard.subcategory_code)


@router.callback_query(StateFilter(FSMFillCard.subcategory_code), MenuCD.filter())
async def process_fill_subcategory(callback: CallbackQuery, state: FSMContext):
    subcategory_code = MenuCD.unpack(callback.data).subcategory_code
    subcategory_name = MenuCD.unpack(callback.data).subcategory_name

    await state.update_data(subcategory_code=subcategory_code, subcategory_name=subcategory_name)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["name"])
    await state.set_state(FSMFillCard.name)


@router.callback_query(StateFilter(FSMFillCard.category_code), Text(text="add_new_category"))
async def handler_process_new_fill_category(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["new_category_code"])
    await callback.answer()
    await state.set_state(FSMFillCard.new_category_code)


@router.message(StateFilter(FSMFillCard.new_category_code), F.text)
async def process_new_fill_category_code(message: Message, state: FSMContext):
    await state.update_data(category_code=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["new_category_name"])
    await state.set_state(FSMFillCard.new_category_name)


@router.message(StateFilter(FSMFillCard.new_category_name), F.text)
async def process_new_fill_category_name(message: Message, state: FSMContext):
    await state.update_data(category_name=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["new_subcategory_code"])
    await state.set_state(FSMFillCard.new_subcategory_code)


@router.callback_query(StateFilter(FSMFillCard.subcategory_code), Text(text="add_new_subcategory"))
async def handler_process_new_fill_subcategory(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["new_subcategory_code"])
    await callback.answer()
    await state.set_state(FSMFillCard.new_subcategory_code)


@router.message(StateFilter(FSMFillCard.new_subcategory_code), F.text)
async def process_new_fill_subcategory_code(message: Message, state: FSMContext):
    await state.update_data(subcategory_code=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["new_subcategory_name"])
    await state.set_state(FSMFillCard.new_subcategory_name)


@router.message(StateFilter(FSMFillCard.new_subcategory_name), F.text)
async def process_new_fill_subcategory_name(message: Message, state: FSMContext):
    await state.update_data(subcategory_name=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["name"])
    await state.set_state(FSMFillCard.name)


@router.message(StateFilter(FSMFillCard.name), F.text)
async def process_fill_photo(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["photo"])
    await state.set_state(FSMFillCard.photo)


@router.message(StateFilter(FSMFillCard.photo), F.photo)
async def process_fill_name(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer(text=LEXICON_FSM_SHOP["price"])
    await state.set_state(FSMFillCard.price)


@router.message(StateFilter(FSMFillCard.price), F.text.isdigit())
async def process_fill_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["time_action"])
    await state.set_state(FSMFillCard.time_action)


@router.message(StateFilter(FSMFillCard.time_action), F.text.isdigit())
async def process_fill_time_action(message: Message, state: FSMContext):
    await state.update_data(time_action=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["description"])
    await state.set_state(FSMFillCard.description)


@router.message(StateFilter(FSMFillCard.description), F.text)
async def process_fill_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    keyboard = create_inline_keyboard(*["Да", "Нет"]).as_markup()
    data = await state.get_data()

    await message.answer(text=LEXICON_FSM_SHOP["done_1"].format(
        category_name=data["category_name"],
        subcategory_name=data["subcategory_name"]))

    await message.answer_photo(photo=data["photo"], caption=LEXICON_FSM_SHOP["done_2"].format(
        name=data["name"], price=data["price"], description=data["description"]), reply_markup=keyboard)


@router.callback_query(StateFilter(FSMFillCard.description),
                       Text(text=["Да", "Нет"]))
async def process_check(callback: CallbackQuery, state: FSMContext):
    if callback.data == "Да":
        data = await state.get_data()
        admin_id_add: types.User = types.User.get_current()
        admin_id_add: int = admin_id_add.id

        await add_item(show=True, category_code=data["category_code"],
                       category_name=data["category_name"], subcategory_name=data["subcategory_name"],
                       subcategory_code=data["subcategory_code"], name=data["name"], photo=data["photo"],
                       price=int(data["price"]), time_action=int(data["time_action"]),
                       description=data["description"], admin_id_add=admin_id_add)

        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_yes"], show_alert=True)

    elif callback.data == "Нет":
        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_no"], show_alert=True)

    await callback.message.delete()

    await callback.message.answer(text=LEXICON_ADMIN['in_admin'],
                                  reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_ADMIN.values())))


@router.message(~StateFilter(default_state))
async def warning_not(message: Message, state: FSMContext):
    state = await state.get_state()
    state = state.split(":")[-1]
    try:
        await message.answer(text=LEXICON_FSM_SHOP["unknown"].format(state=LEXICON_FSM_SHOP[state]))
    except Exception as e:
        await message.answer(text=LEXICON_FSM_SHOP["unknown"].format(state=e))
