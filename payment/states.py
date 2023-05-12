from aiogram.fsm.state import StatesGroup, State


class Payment(StatesGroup):
    payment_select = State()
    payment_input_amount = State()
    payment_qiwi = State()
