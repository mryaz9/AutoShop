from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class BuyItemCD(CallbackData, prefix="admin"):
    item_id: int

def create_inline_keyboard(*args: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button in args:
        kb_builder.row(InlineKeyboardButton(
            text=button,
            callback_data={button}))

    return kb_builder.as_markup()
