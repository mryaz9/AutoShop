from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON


def create_reply_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    # Создаем список списков с кнопками
    keyboard: list[KeyboardButton] = [
        KeyboardButton(text=str(i)) for i in buttons]

    # Инициализируем билдер
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

    builder.row(*keyboard, width=3)

    return builder.as_markup(resize_keyboard=True)


def create_inline_keyboard(*args: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    for button in args:
        kb_builder.row(InlineKeyboardButton(
            text=button,
            callback_data=f'{button}set'))
    # Добавляем в конец клавиатуры кнопку "Назад"
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['back'],
        callback_data='back'))

    kb_builder.row(InlineKeyboardButton(
        text=LEXICON['to_main'],
        callback_data='to_main'))

    return kb_builder.as_markup()
