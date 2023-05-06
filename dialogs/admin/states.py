from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class Admin(StatesGroup):
    see_admin = State()
    add_admin = State()
    del_admin = State()


class Category(StatesGroup):
    edit_categories = State()
    select_categories = State()
    hide_categories = State()
    add_categories = State()
    del_categories = State()


class SubCategory(StatesGroup):
    select_subcategories = State()
    hide_subcategories = State()
    add_subcategories = State()
    del_subcategories = State()


class Product(StatesGroup):
    select_product = State()
    hide_product = State()
    add_product = State()
    del_product = State()


class AddItem(StatesGroup):
    name = State()
    amount = State()
    files = State()
    photo = State()
    price = State()
    time_action = State()
    description = State()

    confirm = State()
