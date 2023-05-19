from aiogram_dialog import Dialog

from handlers.users.assortiment import windows


def items_dialogs():
    return [
        Dialog(
            windows.categories_window(),
            windows.subcategories_window(),
            windows.product_window(),
            windows.product_info_window(),
        ),
        Dialog(
            windows.buy_product_window(),
            windows.confirm_buy_window()
        ),
    ]
