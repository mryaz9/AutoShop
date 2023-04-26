from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from handlers.assortment_handlers import list_categories, list_subcategories, list_items, show_item
from keyboards.kb_menu_item import MenuCD
from keyboards.kb_reply import create_reply_keyboard
from database.command.database_user import add_new_user
from lexicon.lexicon_ru import LEXICON, LEXICON_BUTTON_MAIN


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    database_user = await add_new_user()
    await message.answer(text=f"Привет {database_user.full_name}",
                         reply_markup=create_reply_keyboard(list(LEXICON_BUTTON_MAIN.values())))


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(F.text == LEXICON_BUTTON_MAIN["assortment"])
async def show_menu(message: types.Message):
    # Выполним функцию, которая отправит пользователю кнопки с доступными категориями
    await list_categories(message)


@router.message(F.text == LEXICON_BUTTON_MAIN["profile"])
async def button_profile(message: Message):
    await message.answer(text=LEXICON["profile"])


@router.message(F.text == LEXICON_BUTTON_MAIN["️orders"])
async def button_orders(message: Message):
    await message.answer(text=LEXICON["️orders"])


@router.message(F.text == LEXICON_BUTTON_MAIN["information"])
async def button_information(message: Message):
    await message.answer(text=LEXICON["information"])


@router.callback_query(MenuCD.filter())
async def navigate(call: CallbackQuery, callback_data: MenuCD):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """
    callback_data = dict(callback_data)

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = int(callback_data.get("level"))

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    category = callback_data.get("category")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    subcategory = callback_data.get("subcategory")

    # Получаем айди товара, который выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    item_id = int(callback_data.get("item_id"))

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        0: list_categories,  # Отдаем категории
        1: list_subcategories,  # Отдаем подкатегории
        2: list_items,  # Отдаем товары
        3: show_item  # Предлагаем купить товар
    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        current_level=current_level,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )