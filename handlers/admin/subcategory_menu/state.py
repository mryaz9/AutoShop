from aiogram.fsm.state import StatesGroup, State


class SubCategories(StatesGroup):
    subcategories_menu = State()
    select_categories = State()
    select_subcategories = State()

    input_name_subcategories = State()
    input_photo_subcategories = State()
    add_subcategories = State()
    del_subcategories = State()
