from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

from database.command.database_item import get_subcategories, count_items, get_items, get_categories
from lexicon.lexicon_ru import LEXICON


# Создаем CallbackData-объекты, которые будут нужны для работы с менюшкой

class MenuCD(CallbackData, prefix="show_menu"):
    level: int
    category: str = "0"
    subcategory: str = "0"
    item_id: int = 0


class BuyItemCD(CallbackData, prefix="buy"):
    item_id: int = 0


# Создаем функцию, которая отдает клавиатуру с доступными категориями
async def categories_keyboard() -> InlineKeyboardBuilder:
    # Указываем, что текущий уровень меню - 0
    CURRENT_LEVEL: int = 0

    # Создаем Клавиатуру
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Забираем список товаров из базы данных с РАЗНЫМИ категориями и проходим по нему
    categories = await get_categories()
    for category in categories:
        # Чекаем в базе сколько товаров существует под данной категорией
        number_of_items = await count_items(category.category_code)

        # Сформируем текст, который будет на кнопке
        button_text = f"{category.category_name} ({number_of_items} шт)"

        # Сформируем колбек дату, которая будет на кнопке. Следующий уровень - текущий + 1, и перечисляем категории
        callback_data = MenuCD(level=CURRENT_LEVEL + 1, category=category.category_code).pack()
        # Вставляем кнопку в клавиатуру
        markup.add(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Возвращаем созданную клавиатуру в хендлер
    return markup


# Создаем функцию, которая отдает клавиатуру с доступными подкатегориями, исходя из выбранной категории
async def subcategories_keyboard(category) -> InlineKeyboardBuilder:
    # Текущий уровень - 1
    CURRENT_LEVEL: int = 1
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Забираем список товаров с РАЗНЫМИ подкатегориями из базы данных с учетом выбранной категории и проходим по ним
    subcategories = await get_subcategories(category)
    for subcategory in subcategories:
        # Чекаем в базе сколько товаров существует под данной подкатегорией
        number_of_items = await count_items(category_code=category, subcategory_code=subcategory.subcategory_code)

        # Сформируем текст, который будет на кнопке
        button_text = f"{subcategory.subcategory_name} ({number_of_items} шт)"

        # Сформируем колбек дату, которая будет на кнопке
        callback_data = MenuCD(level=CURRENT_LEVEL + 1, category=category,
                               subcategory=subcategory.subcategory_code).pack()
        markup.add(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    # Создаем Кнопку "Назад", в которой прописываем колбек дату такую, которая возвращает
    # пользователя на уровень назад - на уровень 0.
    return markup


# Создаем функцию, которая отдает клавиатуру с доступными товарами, исходя из выбранной категории и подкатегории
async def items_keyboard(category, subcategory) -> InlineKeyboardBuilder:
    CURRENT_LEVEL: int = 2

    # Устанавливаю row_width = 1, чтобы показывалась одна кнопка в строке на товар
    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()

    # Забираем список товаров из базы данных с выбранной категорией и подкатегорией, и проходим по нему
    items = await get_items(category, subcategory)
    for item in items:
        # Сформируем текст, который будет на кнопке
        button_text = f"{item.name} - ${item.price}"

        # Сформируем колбек дату, которая будет на кнопке
        callback_data = MenuCD(level=CURRENT_LEVEL + 1, category=category,
                               subcategory=subcategory, item_id=item.id).pack()
        markup.add(
            InlineKeyboardButton(
                text=button_text, callback_data=callback_data)
        )

    # Создаем Кнопку "Назад", в которой прописываем колбек дату такую, которая возвращает
    # пользователя на уровень назад - на уровень 1 - на выбор подкатегории
    return markup


# Создаем функцию, которая отдает клавиатуру с кнопками "купить" и "назад" для выбранного товара
def item_keyboard(category, subcategory, item_id) -> InlineKeyboardBuilder:
    CURRENT_LEVEL: int = 3

    markup: InlineKeyboardBuilder = InlineKeyboardBuilder()
    markup.row(
        InlineKeyboardButton(
            text=f"Купить",
            callback_data=BuyItemCD(item_id=item_id).pack()
        )
    )
    return markup


def add_back_and_main(markup: InlineKeyboardBuilder, current_level,
                      category="0", subcategory="0", item_id="0") -> InlineKeyboardMarkup:
    # TODO: Изменить функцию без передачи всех аргументов
    markup.row(
        InlineKeyboardButton(
            text=LEXICON["to_main"],
            callback_data=MenuCD(level=0).pack())
    )
    markup.add(
        InlineKeyboardButton(
            text=LEXICON["back"],
            callback_data=MenuCD(level=current_level - 1, category=category,
                                 subcategory=subcategory, item_id=item_id).pack())
    )
    return markup.as_markup()
