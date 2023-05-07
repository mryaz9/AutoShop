from aiogram.fsm.state import StatesGroup, State


class Assortment(StatesGroup):
    select_categories = State()
    select_subcategories = State()
    select_product = State()
    select_product_info = State()


class BuyProduct(StatesGroup):
    enter_amount = State()
    confirm = State()
