from aiogram.fsm.state import StatesGroup, State


class Mailing(StatesGroup):
    mailing_menu = State()
    create_mailing = State()
