from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class AddItem(StatesGroup):
    categories = State()
    subcategories = State()
    name = State()
    amount = State()
    files = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()

    confirm = State()
