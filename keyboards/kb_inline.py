from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from database.command.database_item import get_categories, count_items, get_subcategories


class MenuCD(CallbackData, prefix="FSM"):
    category_code: str = "0"
    category_name: str = "0"
    subcategory_code: str = "0"
    subcategory_name: str = "0"


async def categories_keyboard() -> InlineKeyboardBuilder:
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    categories = await get_categories()
    for category in categories:
        # Чекаем в базе сколько товаров существует под данной категорией
        number_of_items = await count_items(category.category_code)

        # Сформируем текст, который будет на кнопке
        button_text = f"{category.category_name} ({number_of_items} шт)"

        callback_data = MenuCD(category_code=category.category_code, category_name=category.category_name).pack()
        # Вставляем кнопку в клавиатуру
        markup.add(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


async def subcategories_keyboard(category_code) -> InlineKeyboardBuilder:
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Забираем список товаров с РАЗНЫМИ подкатегориями из базы данных с учетом выбранной категории и проходим по ним
    subcategories = await get_subcategories(category_code)
    for subcategory in subcategories:
        # Чекаем в базе сколько товаров существует под данной подкатегорией
        number_of_items = await count_items(category_code=category_code, subcategory_code=subcategory.subcategory_code)

        # Сформируем текст, который будет на кнопке
        button_text = f"{subcategory.subcategory_name} ({number_of_items} шт)"

        # Сформируем колбек дату, которая будет на кнопке
        callback_data = MenuCD(subcategory_code=subcategory.subcategory_code,
                               subcategory_name=subcategory.subcategory_name).pack()
        markup.add(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )
    return markup


def create_inline_keyboard(*args: str) -> InlineKeyboardBuilder:
    # Создаем объект клавиатуры
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in args:
        markup.row(InlineKeyboardButton(
            text=button,
            callback_data=button))

    return markup
