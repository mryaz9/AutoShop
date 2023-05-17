from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class AddItem(StatesGroup):
    menu = State()
    hide_item = State()

    select_categories = State()
    select_subcategories = State()
    type_item = State()
    name = State()
    amount = State()
    photo = State()
    price = State()
    description = State()

    confirm = State()


class AddCategories(StatesGroup):
    categories_menu = State()
    select_categories = State()
    select_subcategories = State()

    add_categories = State()
    del_categories = State()

    add_subcategories = State()
    del_subcategories = State()


class AddAdmin(StatesGroup):
    admin_menu = State()
    add_admin = State()


class Mailing(StatesGroup):
    mailing_menu = State()
    create_mailing = State()

