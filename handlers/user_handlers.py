from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, callback_query
from typing import Union


from keyboards.kb_menu_item import MenuCD, categories_keyboard, subcategories_keyboard, \
    items_keyboard, item_keyboard
from keyboards.kb_reply import create_reply_keyboard
from database.command_database_item import get_item
from database.command_database_user import add_new_user
from lexicon.lexicon_ru import LEXICON, LEXICON_BUTTON_MAIN

from typing import Union


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


# Та самая функция, которая отдает категории. Она может принимать как CallbackQuery, так и Message
# Помимо этого, мы в нее можем отправить и другие параметры - category, subcategory, item_id,
# Поэтому ловим все остальное в **kwargs
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
    markup = await categories_keyboard()

    # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
    if isinstance(message, Message):
        await message.answer("Смотри, что у нас есть", reply_markup=markup)

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_reply_markup(reply_markup=markup)


# Функция, которая отдает кнопки с подкатегориями, по выбранной пользователем категории
async def list_subcategories(callback: CallbackQuery, category, **kwargs):
    markup = await subcategories_keyboard(category)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_reply_markup(reply_markup=markup)


# Функция, которая отдает кнопки с Названием и ценой товара, по выбранной категории и подкатегории
async def list_items(callback: CallbackQuery, category, subcategory, **kwargs):
    markup = await items_keyboard(category, subcategory)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_text(text="Смотри, что у нас есть", reply_markup=markup)


# Функция, которая отдает уже кнопку Купить товар по выбранному товару
async def show_item(callback: CallbackQuery, category, subcategory, item_id):
    markup = item_keyboard(category, subcategory, item_id)

    # Берем запись о нашем товаре из базы данных
    item = await get_item(item_id)
    text = f"Купи {item.name}"
    await callback.message.edit_text(text=text, reply_markup=markup)


# Функция, которая обрабатывает ВСЕ нажатия на кнопки в этой менюшке
@router.callback_query(MenuCD.filter())
async def navigate(call: CallbackQuery, callback_data: dict):
    """
    :param call: Тип объекта CallbackQuery, который прилетает в хендлер
    :param callback_data: Словарь с данными, которые хранятся в нажатой кнопке
    """

    # Получаем текущий уровень меню, который запросил пользователь
    current_level = callback_data.get("level")

    # Получаем категорию, которую выбрал пользователь (Передается всегда)
    category = callback_data.get("category")

    # Получаем подкатегорию, которую выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    subcategory = callback_data.get("subcategory")

    # Получаем айди товара, который выбрал пользователь (Передается НЕ ВСЕГДА - может быть 0)
    item_id = int(callback_data.get("item_id"))

    # Прописываем "уровни" в которых будут отправляться новые кнопки пользователю
    levels = {
        "0": list_categories,  # Отдаем категории
        "1": list_subcategories,  # Отдаем подкатегории
        "2": list_items,  # Отдаем товары
        "3": show_item  # Предлагаем купить товар
    }

    # Забираем нужную функцию для выбранного уровня
    current_level_function = levels[current_level]

    # Выполняем нужную функцию и передаем туда параметры, полученные из кнопки
    await current_level_function(
        call,
        category=category,
        subcategory=subcategory,
        item_id=item_id
    )