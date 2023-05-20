from aiogram.fsm.state import StatesGroup, State


class AddItem(StatesGroup):
    menu = State()
    add_files = State()
    confirm_add_files = State()
    del_item = State()

    select_categories = State()
    select_subcategories = State()
    select_item = State()
    name = State()
    amount = State()
    photo = State()
    price = State()
    description = State()

    confirm = State()