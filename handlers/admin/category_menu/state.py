from aiogram.fsm.state import StatesGroup, State


class Categories(StatesGroup):
    input_name_categories = State()
    input_photo_categories = State()
    add_categories = State()
    del_categories = State()
