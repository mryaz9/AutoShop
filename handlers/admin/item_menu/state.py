from aiogram.fsm.state import StatesGroup, State


class Item(StatesGroup):
    menu = State()

    del_item = State()

    select_categories = State()
    select_subcategories = State()
    select_item = State()


class AddItem(StatesGroup):
    name = State()
    amount = State()
    photo = State()
    price = State()
    description = State()

    confirm = State()


class AddFiles(StatesGroup):
    add_files = State()
    confirm_add_files = State()
