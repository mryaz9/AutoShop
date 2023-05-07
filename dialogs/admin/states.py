from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class AddItem(StatesGroup):
    select_categories = State()
    select_subcategories = State()
    name = State()
    amount = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()

    confirm = State()
