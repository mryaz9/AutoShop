from aiogram.fsm.state import StatesGroup, State


class Profile(StatesGroup):
    profile = State()


class Purchases(StatesGroup):
    purchases = State()
