from aiogram.fsm.state import StatesGroup, State


class Admin(StatesGroup):
    admin_menu = State()
    add_admin = State()
    view_admin = State()
