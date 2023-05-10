from aiogram.fsm.state import StatesGroup, State


class BotMenu(StatesGroup):
    select_categories = State()
    select_subcategories = State()
    select_product = State()
    select_product_info = State()


class BuyProduct(StatesGroup):
    enter_amount = State()
    confirm = State()


class Payment(StatesGroup):
    payment = State()
    payment_crypto_bot = State()
    payment_qiwi = State()
    payment_balance = State()
    successful = State()

