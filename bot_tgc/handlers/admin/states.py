from aiogram.fsm.state import StatesGroup, State


class AdminMenu(StatesGroup):
    admin_menu = State()


class ChangeMenu(StatesGroup):
    main_menu = State()
    catalog = State()
    order = State()
    profile = State()
    info = State()
    info_about = State()
    confirm = State()


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


class AddCategories(StatesGroup):
    categories_menu = State()
    select_categories = State()
    select_subcategories = State()

    input_name_categories = State()
    input_photo_categories = State()
    add_categories = State()
    del_categories = State()

    input_name_subcategories = State()
    input_photo_subcategories = State()
    add_subcategories = State()
    del_subcategories = State()


class AddAdmin(StatesGroup):
    admin_menu = State()
    add_admin = State()
    view_admin = State()


class Mailing(StatesGroup):
    mailing_menu = State()
    create_mailing = State()
