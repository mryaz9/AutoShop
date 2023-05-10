from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class AddItem(StatesGroup):
    select_categories = State()
    select_subcategories = State()
    type_item = State()
    name = State()
    amount = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()

    confirm = State()


class AddCategories(StatesGroup):
    categories_menu = State()
    select_categories = State()
    add_categories = State()
    add_subcategories = State()


class AddAdmin(StatesGroup):
    admin_menu = State()
    add_admin = State()


class Mailing(StatesGroup):
    mailing_menu = State()
    create_mailing = State()

