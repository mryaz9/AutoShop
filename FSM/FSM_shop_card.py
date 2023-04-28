from aiogram import Router, types
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.state import default_state
from aiogram.filters import Command, Text, StateFilter, or_f
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.utils.keyboard import InlineKeyboardBuilder


from database.command.database_item import add_item
from filters import filters
from keyboards import kb_inline
from database.command import database_item
from keyboards.kb_inline import MenuCD, create_inline_keyboard
from keyboards.kb_reply import create_reply_keyboard
from lexicon.lexicon_ru import LEXICON_BUTTON_ADMIN, LEXICON_FSM_SHOP, LEXICON_ADMIN

router: Router = Router()


router.message.filter(filters.IsAdmin())


class FSMFillCard(StatesGroup):
    fill_category_code = State()
    fill_category_name = State()
    fill_subcategory_code = State()
    fill_subcategory_name = State()
    fill_name = State()
    fill_photo = State()
    fill_price = State()
    fill_time_action = State()
    fill_description = State()


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

    await message.answer(text=LEXICON_FSM_SHOP["category"], reply_markup=markup)
    await state.set_state(FSMFillCard.fill_category_code)


@router.callback_query(StateFilter(FSMFillCard.fill_category_code), MenuCD.filter())
async def process_fill_category(callback: CallbackQuery, state: FSMContext):
    category_code = MenuCD.unpack(callback.data).category_code
    category_name = MenuCD.unpack(callback.data).category_name
    await state.update_data(category=category_code, category_name=category_name)

    markup = add_new_category(await kb_inline.subcategories_keyboard(category_code)).as_markup()
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["subcategory"], reply_markup=markup)
    await state.set_state(FSMFillCard.fill_subcategory_code)


@router.callback_query(StateFilter(FSMFillCard.fill_subcategory_code), MenuCD.filter())
async def process_fill_subcategory(callback: CallbackQuery, state: FSMContext):
    subcategory_code = MenuCD.unpack(callback.data).subcategory_code
    subcategory_name = MenuCD.unpack(callback.data).subcategory_name

    await state.update_data(subcategory_code=subcategory_code, subcategory_name=subcategory_name)
    await callback.message.delete()
    await callback.message.answer(text=LEXICON_FSM_SHOP["name"])
    await state.set_state(FSMFillCard.fill_name)


@router.message(StateFilter(FSMFillCard.fill_name), F.text)
async def process_fill_photo(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=LEXICON_FSM_SHOP["photo"])
    await state.set_state(FSMFillCard.fill_photo)


@router.message(StateFilter(FSMFillCard.fill_photo), F.photo)
async def process_fill_name(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
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
    keyboard = create_inline_keyboard(*["Да", "Нет"]).as_markup()
    data = await state.get_data()
    await message.answer(text=f"{LEXICON_FSM_SHOP['done']} {[*data.values()]}", reply_markup=keyboard)


@router.callback_query(StateFilter(FSMFillCard.fill_description),
                       Text(text=["Да", "Нет"]))
async def process_check(callback: CallbackQuery, state: FSMContext):
    if callback.data == "Да":
        data = await state.get_data()
        admin_id_add = types.User.get_current()

        await add_item(show=True, category_code=data["category_code"],
                       category_name=data["category_name"], subcategory_name=["subcategory_name"],
                       subcategory_code=data["subcategory_code"], name=data["name"], photo=data["photo"],
                       price=data["price"], description=data["description"], admin_id_add=admin_id_add)

        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_yes"], show_alert=True)

    elif callback.data == "Нет":
        await state.clear()
        await callback.answer(text=LEXICON_FSM_SHOP["done_no"], show_alert=True)

    await callback.message.delete()


@router.message(~StateFilter(default_state))
async def warning_not(message: Message):
    await message.answer(text=LEXICON_FSM_SHOP["unknown"])


def add_new_category(markup: InlineKeyboardBuilder) -> InlineKeyboardBuilder:
    markup.row(
        InlineKeyboardButton(
            text=LEXICON_FSM_SHOP["add_new_category"],
            callback_data="add_new_category"
        )
    )
    return markup
