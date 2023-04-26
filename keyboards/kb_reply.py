from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_reply_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    # Создаем список списков с кнопками
    keyboard: list[KeyboardButton] = [
        KeyboardButton(text=str(i)) for i in buttons]

    # Инициализируем билдер
    builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

    builder.row(*keyboard, width=3)

    return builder.as_markup(resize_keyboard=True)
