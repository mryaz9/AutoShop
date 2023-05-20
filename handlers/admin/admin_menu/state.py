from aiogram.fsm.state import StatesGroup, State


class AddAdmin(StatesGroup):
    admin_menu = State()
    add_admin = State()
    view_admin = State()
