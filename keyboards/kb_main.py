from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_BUTTON_MAIN


def create_keyboard_main() -> ReplyKeyboardMarkup:
    # Создаем список списков с кнопками
    keyboard: list[KeyboardButton] = [
        KeyboardButton(text=str(i)) for i in LEXICON_BUTTON_MAIN.values()]

    # Инициализируем билдер
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

    builder.row(*keyboard, width=3)

    my_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)

    return my_keyboard
