from typing import Union

from aiogram.types import CallbackQuery, Message

from database.command.database_item import get_item
from keyboards.kb_menu_item import categories_keyboard, add_back_and_main, subcategories_keyboard, items_keyboard, \
    item_keyboard
from lexicon.lexicon_ru import LEXICON_INLINE_MENU


# Та самая функция, которая отдает категории. Она может принимать как CallbackQuery, так и Message
# Помимо этого, мы в нее можем отправить и другие параметры - category_code, subcategory, item_id,
# Поэтому ловим все остальное в **kwargs
async def list_categories(message: Union[CallbackQuery, Message], **kwargs):
    # Клавиатуру формируем с помощью следующей функции (где делается запрос в базу данных)
    markup = await categories_keyboard()

    # Проверяем, что за тип апдейта. Если Message - отправляем новое сообщение
    if isinstance(message, Message):
        await message.answer(text=LEXICON_INLINE_MENU["category_code"], reply_markup=markup.as_markup())

    # Если CallbackQuery - изменяем это сообщение
    elif isinstance(message, CallbackQuery):
        call = message
        await call.message.edit_text(text=LEXICON_INLINE_MENU["category_code"], reply_markup=markup.as_markup())


# Функция, которая отдает кнопки с подкатегориями, по выбранной пользователем категории
async def list_subcategories(callback: CallbackQuery, current_level, category, **kwargs):
    markup = add_back_and_main(await subcategories_keyboard(category), current_level, category)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_text(text=LEXICON_INLINE_MENU["subcategory"], reply_markup=markup)


# Функция, которая отдает кнопки с Названием и ценой товара, по выбранной категории и подкатегории
async def list_items(callback: CallbackQuery, current_level, category, subcategory, **kwargs):
    markup = add_back_and_main(await items_keyboard(category, subcategory), current_level, category, subcategory)

    # Изменяем сообщение, и отправляем новые кнопки с подкатегориями
    await callback.message.edit_text(text=LEXICON_INLINE_MENU["name"], reply_markup=markup)


# Функция, которая отдает уже кнопку Купить товар по выбранному товару
async def show_item(callback: CallbackQuery, current_level, category, subcategory, item_id):
    markup = add_back_and_main(item_keyboard(category, subcategory, item_id),
                               current_level, category, subcategory, item_id)

    # Берем запись о нашем товаре из базы данных
    item = await get_item(item_id)
    text = f"{LEXICON_INLINE_MENU['card']} {item.name}"
    await callback.message.edit_text(text=text, reply_markup=markup)
