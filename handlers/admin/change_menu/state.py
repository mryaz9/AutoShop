from aiogram.fsm.state import StatesGroup, State


class ChangeMenu(StatesGroup):
    main_menu = State()
    catalog = State()
    order = State()
    profile = State()
    info = State()
    info_about = State()
    confirm = State()
