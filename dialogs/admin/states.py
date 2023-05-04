from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    select_categories = State()
    select_subcategories = State()
    select_product = State()
