from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class AddAssortiment(StatesGroup):
    select_categories = State()
    add_new_categories_code = State()
    add_new_categories_name = State()

    select_subcategories = State()
    add_new_subcategories_code = State()
    add_new_subcategories_name = State()

    name = State()
    amount = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()

    confirm = State()
